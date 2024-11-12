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
  analog_value: number;
  voltage: number;
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
  const [data, setData] = useState<ADC[]>([]);
  const [isClient, setIsClient] = useState(false);

  // Check if component is mounted on the client
  useEffect(() => {
    setIsClient(true);
  }, []);

  async function fetchData() {
    console.log("FechData");
    try {
      const response = await axios.get("http://127.0.0.1:8000/get_sensorADC");
      console.log("Fetched data:", response.data); // Check the structure here
      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  useEffect(() => {
    fetchData();
    const interval = setInterval(() => {
      fetchData();
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  if (!isClient) return null; // Prevent rendering on the server side

  const formattedData = data.map((item) => ({
    ...item,
    fecha: new Date(item.fecha).toLocaleTimeString(), // Format date as time
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
        <section id="visualizacion-sensores" className="section">
            <h2>Datos de Sensores</h2>
            <p>A continuación se presentan las gráficas de los datos recopilados de los diferentes sensores del carrito IoT.</p>
            
            <div className="sensor-graficas">
                <div className="sensor-grafico">
                  <h3>Sensor ADC</h3>
                  <ResponsiveContainer width="100%" height={250}>
                    <LineChart data={formattedData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="fecha" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" dataKey="voltage" stroke="#ff7043" />
                      <Line type="monotone" dataKey="analog_value" stroke="#4CAF50" />
                    </LineChart>
                  </ResponsiveContainer>

                </div>

                <div className="sensor-grafico">
                    <h3>Sensor Acelerometro</h3>
                    <ResponsiveContainer width="100%" height={250}>
                    <LineChart data={formattedData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="fecha" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" dataKey="voltage" stroke="#ff7043" />
                      <Line type="monotone" dataKey="analog_value" stroke="#4CAF50" />
                    </LineChart>
                  </ResponsiveContainer>
                </div>

                <div className="sensor-grafico">
                    <h3>Sensor BME</h3>
                    <ResponsiveContainer width="100%" height={250}>
                    <LineChart data={formattedData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="fecha" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" dataKey="voltage" stroke="#ff7043" />
                      <Line type="monotone" dataKey="analog_value" stroke="#4CAF50" />
                    </LineChart>
                  </ResponsiveContainer>
                </div>

                <div className="sensor-grafico">
                    <h3>Sensor de Distancia</h3>
                    <ResponsiveContainer width="100%" height={250}>
                    <LineChart data={formattedData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="fecha" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      <Line type="monotone" dataKey="voltage" stroke="#ff7043" />
                      <Line type="monotone" dataKey="analog_value" stroke="#4CAF50" />
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
