"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";

interface ADC {
  id: number;
  valor_analogico: number;
  voltaje: number;
  fecha: string;
}

interface Acelerometro {
  id: number;
  x_cor: number;
  y_cor: number;
  z_cor: number;
  fecha: string;
}

interface Distancia {
  id: number;
  dist_cm: number;
  fecha: string;
}

interface BME {
  id: number;
  temp: number;
  presion: number;
  altitud: number;
  fecha: string;
}

export default function Home() {
  const [adcData, setAdcData] = useState<ADC[]>([]);
  const [acelerometroData, setAcelerometroData] = useState<Acelerometro[]>([]);
  const [distanciaData, setDistanciaData] = useState<Distancia[]>([]);
  const [bmeData, setBmeData] = useState<BME[]>([]);
  const [isClient, setIsClient] = useState(false);
  const [lastHours, setLastHours] = useState(false);
  const [activeKey, setActiveKey] = useState<string | null>(null); 
  const [status, setStatus] = useState<string>(""); 

  useEffect(() => {
    setIsClient(true);
  }, []);

  const handleKeyPress = (command: string) => {
    if (["w", "a", "s", "d", "stop"].includes(command) && command !== activeKey) {
      setActiveKey(command);
      controlarCarrito(command);
      if(command == "stop"){
        setStatus(`Car Stopped`);
      } else {
        setStatus(`Moving ${command.toUpperCase()}`);
      }
    }
  };

  function getlastHours() {
    const date = new Date();
    date.setHours(date.getHours() - 24); 
    return date.toISOString(); 
  }

  const controlarCarrito = (comando: string) => {
    fetch('http://127.0.0.1:8000/Movimiento', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ comando }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => console.log('Respuesta del backend:', data))
      .catch((error) => console.error('Error al controlar el carrito:', error));
  };

  async function fetchAdcData() {
    try {
      const params = new URLSearchParams();
      if (lastHours) {
        params.append("fecha_inicio", getlastHours());
      }
      const response = await axios.get("http://127.0.0.1:8000/get_sensorADC", { params });
      setAdcData(response.data);
    } catch (error) {
      console.error("Error fetching ADC data:", error);
    }
  }

  async function fetchAcelerometroData() {
    try {
      const params = new URLSearchParams();
      if (lastHours) {
        params.append("fecha_inicio", getlastHours());
      }
      const response = await axios.get("http://127.0.0.1:8000/get_sensorAcelerometro", { params });
      setAcelerometroData(response.data);
    } catch (error) {
      console.error("Error fetching Acelerometro data:", error);
    }
  }

  async function fetchDistanciaData() {
    try {
      const params = new URLSearchParams();
      if (lastHours) {
        params.append("fecha_inicio", getlastHours());
      }
      const response = await axios.get("http://127.0.0.1:8000/get_sensorDistancia", { params });
      setDistanciaData(response.data);
    } catch (error) {
      console.error("Error fetching Distancia data:", error);
    }
  }

  async function fetchBmeData() {
    try {
      const params = new URLSearchParams();
      if (lastHours) {
        params.append("fecha_inicio", getlastHours());
      }
      const response = await axios.get("http://127.0.0.1:8000/get_sensorBME", { params });
      setBmeData(response.data);
    } catch (error) {
      console.error("Error fetching BME data:", error);
    }
  }

  useEffect(() => {
    fetchAdcData();
    fetchAcelerometroData();
    fetchDistanciaData();
    fetchBmeData();

    const interval = setInterval(() => {
      fetchAdcData();
      fetchAcelerometroData();
      fetchDistanciaData();
      fetchBmeData();
    }, 5000);

    console.log("lastHours changed:", lastHours);

    return () => clearInterval(interval);
  }, [lastHours]);

  if (!isClient) return null;

  const formattedAdcData = adcData.map((item) => ({
    ...item,
    fecha: new Date(item.fecha).toLocaleTimeString(),
  }));

  const formattedAcelerometroData = acelerometroData.map((item) => ({
    ...item,
    fecha: new Date(item.fecha).toLocaleTimeString(),
  }));

  const formattedDistanciaData = distanciaData.map((item) => ({
    ...item,
    fecha: new Date(item.fecha).toLocaleTimeString(),
  }));

  const formattedBmeData = bmeData.map((item) => ({
    ...item,
    fecha: new Date(item.fecha).toLocaleTimeString(),
  }));

  return (
    <>
      <header>
        <h1>Proyecto IoT</h1>
        <nav>
          <a href="#documentacion">Documentación</a>
          <a href="#visualizacion-sensores">Datos de Sensores</a>
        </nav>
      </header>

      <div className="container">

        <section id="control-carrito" className="section">
          <h2>Control del Carrito</h2>
          <p>Utiliza los controles a continuación o las teclas <strong>W, A, S, D</strong> en tu teclado para controlar el carrito.</p>
          <div id="carrito-controles">
            <div className="fila">
              <button className="control-button" onClick={() => handleKeyPress('w') }>W</button>
            </div>
            <div className="fila">
              <button className="control-button" onClick={() => handleKeyPress('a') }>A</button>
              <button className="control-button" onClick={() => handleKeyPress('s') }>S</button>
              <button className="control-button" onClick={() => handleKeyPress('d') }>D</button>
            </div>
            <div>
              <button className="control-button" onClick={() => handleKeyPress('stop') }>STOP</button>
            </div>
          </div>
          <p>Status: {status}</p>
        </section>

        <section id="visualizacion-sensores" className="section">
          <h2>Datos de Sensores</h2>
          <p>A continuación se presentan las gráficas de los datos recopilados de los diferentes sensores del carrito IoT.</p>

          <div id="filtro">
            <button className="button" onClick={() => setLastHours(true)}>  Filtrar al ultimo día  </button>
            <button className="button" onClick={() => setLastHours(false)}>   Datos Historico  </button>
          </div>

          <div className="sensor-graficas">
            <div className="sensor-grafico">
              <h3>Sensor ADC</h3>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={formattedAdcData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fecha" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="voltaje" stroke="#ff7043" />
                  <Line type="monotone" dataKey="valor_analogico" stroke="#4CAF50" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="sensor-grafico">
              <h3>Sensor Acelerometro</h3>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={formattedAcelerometroData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fecha" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="x_cor" stroke="#ff7043" />
                  <Line type="monotone" dataKey="y_cor" stroke="#4CAF50" />
                  <Line type="monotone" dataKey="z_cor" stroke="#42A5F5" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="sensor-grafico">
              <h3>Sensor BME</h3>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={formattedBmeData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fecha" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="temp" stroke="#ff7043" />
                  <Line type="monotone" dataKey="presion" stroke="#4CAF50" />
                  <Line type="monotone" dataKey="altitud" stroke="#42A5F5" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="sensor-grafico">
              <h3>Sensor de Distancia</h3>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={formattedDistanciaData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fecha" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="dist_cm" stroke="#ff7043" />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        </section>

        <section id="documentacion" className="section">
          <h2>Documentación Técnica</h2>
          <p>Accede a la documentación detallada del proyecto, incluyendo esquemas, circuitos y código.</p>
          <a href="https://github.com/2003gdb/proyecto_Iot/" className="button">Descargar Documentación</a>
        </section>
      </div>

      <footer>
        <p>© 2023 Proyecto IoT - Todos los derechos reservados</p>
      </footer>
    </>
  );
}
