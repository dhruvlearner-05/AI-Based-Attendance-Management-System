import streamlit as st
def footer_home():
    st.markdown("""
            <div style='margin-top:2rem;display:flex;gap:6px;align-items:center;justify-content:center;'>
                <p style='text-align:center;color:#E0E3FF;font-size:14px;'>© 2026 AttendAI. All rights reserved.</p>
            </div>
               """,unsafe_allow_html=True)       
def footer_dashboard():
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;">© 2026 AttendAI. All rights reserved.</p>  
        </div>
                
                """, unsafe_allow_html=True)