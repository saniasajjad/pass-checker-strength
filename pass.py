import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")
    
    # Upper and lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")
    
    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")
    
    # Common password patterns check
    common_patterns = ["password", "1234", "qwerty", "abc", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        strength = max(0, strength - 2)
        feedback.append("Avoid common words and sequences (e.g., 'password', '1234').")
    
    return strength, feedback

# Streamlit UI
st.title("🔑 Welcome to the Ultimate Password Strength Checker! 👋")
st.write("🔒 **Protect your accounts with a strong password!** This tool helps you check your password strength and provides expert tips to improve it. A strong password keeps your personal and financial information safe from hackers. Let's create a **bulletproof password** today! 🚀")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    if strength <= 2:
        st.error("Weak Password 🔴")
    elif strength <= 4:
        st.warning("Moderate Password 🟠")
    else:
        st.success("Strong Password 🟢")
    
    st.write("### Feedback:")
    for msg in feedback:
        st.write(f"- {msg}")

