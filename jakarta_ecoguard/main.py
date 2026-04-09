import os
import sys
import sqlite3
import json
from datetime import datetime
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai.llms.providers.gemini.completion import GeminiCompletion
from crewai.tools import tool
import requests

load_dotenv()

# force UTF-8 output on Windows so CrewAI emoji/log handlers do not crash
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ========================= CONFIG =========================
GEMINI_MODEL = "gemini-2.5-flash"
JAKARTA_LAT = -6.2088
JAKARTA_LON = 106.8456

# SQLite untuk transparansi & audit log (wajib etika)
def init_db():
    conn = sqlite3.connect("eco_guard.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS actions (
            timestamp TEXT,
            agent TEXT,
            action TEXT,
            reasoning TEXT,
            impact TEXT
        )
    """)
    conn.commit()
    return conn

# Custom Tool: Fetch Real-time AQI Jakarta (OpenWeatherMap - free)
@tool
def fetch_aqi_tool() -> str:
    """Fetch real-time air quality index (AQI) data for Jakarta from OpenWeatherMap API."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={JAKARTA_LAT}&lon={JAKARTA_LON}&appid={api_key}"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        aqi = data["list"][0]["main"]["aqi"]  # 1=Good, 5=Very Poor
        components = data["list"][0]["components"]
        return json.dumps({
            "timestamp": datetime.now().isoformat(),
            "aqi": aqi,
            "pm25": round(components.get("pm2_5", 0), 2),
            "pm10": round(components.get("pm10", 0), 2),
            "no2": round(components.get("no2", 0), 2),
            "so2": round(components.get("so2", 0), 2),
            "interpretation": {1:"Baik", 2:"Cukup", 3:"Sedang", 4:"Buruk", 5:"Sangat Buruk"}.get(aqi, "Ekstrem")
        })
    except Exception as e:
        return f"Error fetching AQI: {str(e)}"

# ========================= LLM =========================
llm = GeminiCompletion(
    model=GEMINI_MODEL,
    temperature=0.3,
    api_key=os.getenv("GOOGLE_API_KEY")
)

# ========================= AGENTS =========================
monitor_agent = Agent(
    role="Air Quality Monitor",
    goal="Memantau polusi udara Jakarta secara real-time dan akurat",
    backstory="Anda adalah sensor cerdas yang selalu update data lingkungan Jakarta.",
    llm=llm,
    verbose=True,
    tools=[fetch_aqi_tool]
)

predictor_agent = Agent(
    role="Risk Predictor",
    goal="Memprediksi risiko polusi 24 jam ke depan dan dampak kesehatan",
    backstory="Anda ahli analisis tren polusi dan kesehatan masyarakat Jakarta.",
    llm=llm,
    verbose=True
)

equity_agent = Agent(
    role="Social Equity Analyst",
    goal="Memastikan semua rekomendasi berkeadilan dan inklusif bagi kelompok rentan",
    backstory="Anda fokus pada keadilan iklim: anak-anak, lansia, dan warga miskin di Jakarta Utara & Timur.",
    llm=llm,
    verbose=True
)

coordinator_agent = Agent(
    role="Action Coordinator",
    goal="Mengkoordinasikan tindakan otonom, mencatat semua keputusan, dan memastikan transparansi",
    backstory="Anda pemimpin tim yang bertanggung jawab, selalu mencatat alasan & dampak.",
    llm=llm,
    verbose=True
)

# ========================= TASKS =========================
task1 = Task(
    description="Ambil data AQI Jakarta terkini menggunakan tool. Berikan data mentah lengkap.",
    expected_output="JSON data AQI + interpretasi",
    agent=monitor_agent
)

task2 = Task(
    description="Prediksi risiko polusi 24 jam ke depan berdasarkan data terkini. Sertakan level bahaya dan kelompok yang paling terdampak.",
    expected_output="Prediksi + alasan ilmiah",
    agent=predictor_agent
)

task3 = Task(
    description="Analisis dampak sosial dan usulkan rekomendasi yang adil (prioritas kelompok rentan di Jakarta). Pastikan inklusi dan keadilan.",
    expected_output="Rekomendasi equity-focused",
    agent=equity_agent
)

task4 = Task(
    description="Koordinasikan semua hasil menjadi rencana aksi otonom. Catat keputusan, alasan, dan dampak terukur. Simpan ke database.",
    expected_output="Rencana aksi lengkap + log transparansi",
    agent=coordinator_agent,
    context=[task1, task2, task3]
)

# ========================= CREW =========================
crew = Crew(
    agents=[monitor_agent, predictor_agent, equity_agent, coordinator_agent],
    tasks=[task1, task2, task3, task4],
    process=Process.sequential,   # urut tapi tetap kolaboratif
    verbose=True,
    memory=False,
    tracing=True
)

# ========================= RUN =========================
if __name__ == "__main__":
    print("Menjalankan Jakarta EcoGuard AI - Gemini 2.5 Flash...")
    db = init_db()
    
    result = crew.kickoff()
    
    print("\nHASIL AGENTIC AI:")
    print(result)
    
    # Simpan log ke SQLite untuk transparansi
    conn = db
    conn.execute("""
        INSERT INTO actions (timestamp, agent, action, reasoning, impact)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        "Coordinator Agent",
        "Rencana Aksi Final",
        str(result)[:500],  # ringkasan
        "Dampak: Rekomendasi equity untuk ribuan warga Jakarta rentan"
    ))
    conn.commit()
    conn.close()
    
    print("\nLog disimpan di eco_guard.db (transparansi & audit trail)")
    print("Sistem siap demo untuk kompetisi!")