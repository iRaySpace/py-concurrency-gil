import React, { useState, useRef } from 'react'
import { Line } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'
import './App.css'
import api from './api'

ChartJS.register(
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend,
)

const INTERVAL_SECS = 3000

function App() {
  const intervalRef = useRef(null)
  const [isPlaying, setIsPlaying] = useState(false)
  const [dataPoints, setDataPoints] = useState([])

  const fetchInfo = async () => {
    try {
      const res = await api.get('/info')
      setDataPoints((prev) => [
        ...prev,
        {
          time: new Date().toLocaleTimeString(),
          activeCount: res.data['active_count'],
          existingCount: res.data['existing_count'],
        }
      ])
    } catch (err) {
      console.error('Error fetching info:', err.message);
    }
  }

  const startPolling = () => {
    intervalRef.current = setInterval(fetchInfo, INTERVAL_SECS)
    setIsPlaying(true)
  }

  const stopPolling = () => {
    clearInterval(intervalRef.current)
    setIsPlaying(false)
  }

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Game Player Stats' },
    },
  }

  const chartData = {
    labels: dataPoints.map((d) => d.time),
    datasets: [
      {
        label: 'Active Player Count',
        borderColor: 'rgb(75, 192, 192)',
        data: dataPoints.map((d) => d.activeCount),
      },
      {
        label: 'Existing Player Count',
        borderColor: 'rgb(255, 99, 132)',
        data: dataPoints.map((d) => d.existingCount),
      },
    ],
  }

  return (
    <>
      <h1>py-concurrency-gil</h1>
      <p>Simulating concurrency problems via "game simulation"</p>
      <button
        onClick={!isPlaying ? startPolling : stopPolling}
        className={`btn-animate ${isPlaying ? "playing" : ""}`}
        style={{
          marginTop: "1em",
          backgroundColor: !isPlaying ? "#4ade80" : "#f87171",
        }}
      >
        {!isPlaying ? "Start" : "Stop"}
      </button>
      <div style={{ marginTop: "1.5em" }}>
        <Line options={options} data={chartData} />
      </div>
    </>
  )
}

export default App
