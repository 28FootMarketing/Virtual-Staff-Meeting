import sys
import os
import streamlit as st

# ✅ Ensure agents module can be imported
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

try:
    import agents.jordan as jordan
    import agents.kobe as kobe
    import agents.maya as maya
    import agents.magic as magic
    import agents.lisa as lisa
    import agents.dawn as dawn
    import agents.bill as bill
except ModuleNotFoundError as e:
    st.error(f"❌ Import error: {e}")
    st.stop()

# ✅ Page setup
st.set_page_config(page_title="Virtual Staff Meeting", layout="centered")
st.title("🏀 Weekly Recruiting Staff Meeting")

# ✅ Define agent list
agent_list = {
    "Jordan": jordan.status_report,
    "Kobe": kobe.status_report,
    "Maya": maya.status_report,
    "Magic": magic.status_report,
    "Lisa": lisa.status_report,
    "Dawn": dawn.status_report,
    "Bill": bill.status_report
}

# ✅ Render agent reports
for name, report_func in agent_list.items():
    with st.expander(f"🧠 {name}'s Report", expanded=False):
        try:
            report_func()
        except Exception as err:
            st.error(f"❌ Error loading {name}'s report: {err}")
