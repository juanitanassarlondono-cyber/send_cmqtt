import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Configuración de página
st.set_page_config(
    page_title="MQTT Control",
    page_icon="📡",
    layout="wide"
)

# Estilos visuales
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #030B1F 0%, #061B45 45%, #003B8E 100%);
    color: #F8FAFC;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020817 0%, #061B45 100%);
    border-right: 1px solid rgba(0, 212, 255, 0.35);
}

section[data-testid="stSidebar"] * {
    color: #F8FAFC !important;
}

.hero-card {
    background: linear-gradient(135deg, rgba(0, 119, 255, 0.28), rgba(0, 212, 255, 0.12));
    border: 1px solid rgba(0, 212, 255, 0.35);
    border-radius: 28px;
    padding: 34px 38px;
    box-shadow: 0 24px 70px rgba(0, 0, 0, 0.35);
    margin-bottom: 28px;
}

.hero-label {
    display: inline-block;
    background: rgba(0, 212, 255, 0.14);
    border: 1px solid rgba(0, 212, 255, 0.45);
    color: #8DEBFF;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
    letter-spacing: 0.4px;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    line-height: 1.05;
    color: #FFFFFF;
    margin-bottom: 12px;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-size: 18px;
    line-height: 1.6;
    color: #D7E9FF;
    max-width: 850px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.075);
    border: 1px solid rgba(148, 197, 255, 0.22);
    border-radius: 24px;
    padding: 26px;
    box-shadow: 0 16px 45px rgba(0, 0, 0, 0.22);
    margin-bottom: 22px;
}

.card-title {
    font-size: 22px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.card-text {
    font-size: 15px;
    color: #CFE8FF;
    line-height: 1.6;
}

.step-badge {
    display: inline-block;
    background: rgba(0, 119, 255, 0.18);
    border: 1px solid rgba(0, 212, 255, 0.42);
    color: #9EEBFF;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 12px;
}

.status-card {
    background: linear-gradient(135deg, rgba(0, 119, 255, 0.22), rgba(0, 212, 255, 0.08));
    border: 1px solid rgba(0, 212, 255, 0.30);
    border-radius: 22px;
    padding: 22px;
    margin-bottom: 18px;
}

.status-title {
    font-size: 18px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 6px;
}

.status-text {
    color: #D7E9FF;
    font-size: 14px;
    line-height: 1.5;
}

div.stButton > button {
    background: linear-gradient(135deg, #0077FF 0%, #00D4FF 100%);
    color: #FFFFFF;
    border: none;
    border-radius: 16px;
    padding: 0.8rem 1.2rem;
    font-weight: 800;
    font-size: 16px;
    box-shadow: 0 14px 34px rgba(0, 119, 255, 0.38);
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 42px rgba(0, 212, 255, 0.38);
    color: #FFFFFF;
}

div.stButton > button:active {
    transform: translateY(0px);
}

[data-testid="stSlider"] label {
    color: #D7E9FF !important;
    font-weight: 700;
}

[data-testid="stSlider"] {
    color: #FFFFFF;
}

.stAlert {
    border-radius: 16px;
}

hr {
    border-color: rgba(0, 212, 255, 0.25);
}

.small-note {
    color: #A9C7EA;
    font-size: 14px;
    line-height: 1.5;
}

.python-version {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(0, 212, 255, 0.25);
    border-radius: 18px;
    padding: 16px 20px;
    color: #D7E9FF;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


# Muestra la versión de Python junto con detalles adicionales
st.markdown(
    f"""
    <div class="python-version">
        <strong>Versión de Python:</strong> {platform.python_version()}
    </div>
    """,
    unsafe_allow_html=True
)

values = 0.0
act1 = "OFF"


def on_publish(client, userdata, result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass


def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)


broker = "157.230.214.127"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message


# Sidebar informativo
with st.sidebar:
    st.markdown("## ⚙️ Configuración MQTT")

    st.markdown("""
    <div class="small-note">
        Esta app publica comandos digitales y valores analógicos hacia un broker MQTT.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📡 Broker")
    st.markdown(f"""
    <div class="status-card">
        <div class="status-title">Servidor MQTT</div>
        <div class="status-text">
            <strong>Broker:</strong> {broker}<br>
            <strong>Puerto:</strong> {port}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧭 Tópicos usados")
    st.markdown("""
    - `cmqtt_s` para comandos ON/OFF  
    - `cmqtt_a` para valores analógicos
    """)

    st.divider()

    st.markdown("""
    <div class="small-note">
        Consejo: verifica que tu dispositivo en Wokwi, Arduino o ESP32 esté suscrito a los mismos tópicos.
    </div>
    """, unsafe_allow_html=True)


# Header principal
st.markdown("""
<div class="hero-card">
    <div class="hero-label">IOT MQTT CONTROL PANEL</div>
    <div class="hero-title">MQTT Control</div>
    <div class="hero-subtitle">
        Panel de control para enviar comandos digitales y valores analógicos mediante MQTT.
        Ideal para pruebas con Arduino, ESP32, Wokwi y aplicaciones IoT conectadas.
    </div>
</div>
""", unsafe_allow_html=True)


# Estructura principal
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown("""
    <div class="glass-card">
        <span class="step-badge">CONTROL DIGITAL</span>
        <div class="card-title">Activar o apagar dispositivo</div>
        <div class="card-text">
            Usa estos botones para publicar el estado digital del actuador en el tópico MQTT configurado.
        </div>
    </div>
    """, unsafe_allow_html=True)

    btn_on, btn_off = st.columns(2)

    with btn_on:
        if st.button('🟢 ON', use_container_width=True):
            act1 = "ON"
            client1 = paho.Client("GIT-HUB")
            client1.on_publish = on_publish
            client1.connect(broker, port)
            message = json.dumps({"Act1": act1})
            ret = client1.publish("cmqtt_s", message)

            #client1.subscribe("Sensores")

        else:
            st.write('')

    with btn_off:
        if st.button('🔴 OFF', use_container_width=True):
            act1 = "OFF"
            client1 = paho.Client("GIT-HUB")
            client1.on_publish = on_publish
            client1.connect(broker, port)
            message = json.dumps({"Act1": act1})
            ret = client1.publish("cmqtt_s", message)

        else:
            st.write('')

with right_col:
    st.markdown("""
    <div class="glass-card">
        <span class="step-badge">CONTROL ANALÓGICO</span>
        <div class="card-title">Enviar valor variable</div>
        <div class="card-text">
            Ajusta el valor con el slider y envíalo al tópico MQTT para controlar intensidad, velocidad, temperatura simulada u otra variable.
        </div>
    </div>
    """, unsafe_allow_html=True)

    values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
    st.write('Values:', values)

    if st.button('📤 Enviar valor analógico', use_container_width=True):
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Analog": float(values)})
        ret = client1.publish("cmqtt_a", message)

    else:
        st.write('')


# Sección inferior de explicación
st.divider()

st.markdown("""
<div class="glass-card">
    <span class="step-badge">RESUMEN DE FUNCIONAMIENTO</span>
    <div class="card-title">¿Qué hace esta aplicación?</div>
    <div class="card-text">
        Esta interfaz permite publicar mensajes MQTT desde Streamlit. 
        Los botones <strong>ON</strong> y <strong>OFF</strong> envían un comando digital al tópico <strong>cmqtt_s</strong>.
        El slider permite enviar un valor numérico al tópico <strong>cmqtt_a</strong>.
        La estructura visual fue reorganizada para separar claramente el control digital, el control analógico y la información de conexión.
    </div>
</div>
""", unsafe_allow_html=True)
