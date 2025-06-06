import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import agents.jordan as jordan
import agents.kobe as kobe
import agents.maya as maya
import agents.magic as magic
import agents.lisa as lisa
import agents.dawn as dawn
import agents.bill as bill

st.set_page_config(page_title="Virtual Staff Meeting", layout="centered")
st.title("🏀 Weekly Recruiting Staff Meeting")

agents = {
    "Jordan": jordan.status_report,
    "Kobe": kobe.status_report,
    "Maya": maya.status_report,
    "Magic": magic.status_report,
    "Lisa": lisa.status_report,
    "Dawn": dawn.status_report,
    "Bill": bill.status_report
}

for name, report_func in agents.items():
    with st.expander(f"🧠 {name}'s Report", expanded=False):
        report_func()
