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
  const [adcData, setAdcData] = useState<ADC[]>([]);
  const [acelerometroData, setAcelerometroData] = useState<Acelerometro[]>([]);
  const [distanciaData, setDistanciaData] = useState<Distancia[]>([]);
  const [bmeData, setBmeData] = useState<BME[]>([]);
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  async function fetchAdcData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/get_sensorADC");
      setAdcData(response.data);
    } catch (error) {
      console.error("Error fetching ADC data:", error);
    }
  }

  async function fetchAcelerometroData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/get_sensorAcelerometro");
      setAcelerometroData(response.data);
    } catch (error) {
      console.error("Error fetching Acelerometro data:", error);
    }
  }

  async function fetchDistanciaData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/get_sensorDistancia");
      setDistanciaData(response.data);
    } catch (error) {
      console.error("Error fetching Distancia data:", error);
    }
  }

  async function fetchBmeData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/get_sensorBME");
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
    }, 2000);

    return () => clearInterval(interval);
  }, []);

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
        <section id="visualizacion-sensores" className="section">
          <h2>Datos de Sensores</h2>
          <p>A continuación se presentan las gráficas de los datos recopilados de los diferentes sensores del carrito IoT.</p>

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
                  <Line type="monotone" dataKey="voltage" stroke="#ff7043" />
                  <Line type="monotone" dataKey="analog_value" stroke="#4CAF50" />
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
