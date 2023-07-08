import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

const API_URL = "http://0.0.0.0:8000";

function App() {
  const [loaded, setLoaded] = useState([]);

  const handleChange = (fileInput: any) => {
    console.log(fileInput);
    const file = fileInput[0];
    const formData = new FormData();
    formData.append("file", file);
    fetch(API_URL + "/product/file", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("File upload failed");
        }
      })
      .then((data) => {
        setLoaded(data);
        console.log("Server response:", data);
      })
      .catch((error) => {
        console.error("Error uploading file:", error);
      });
  };

  return (
    <div className="App">
      {loaded.length > 0 ? (
        <table>
          <tr>
            <th>Type</th>
            <th>Date</th>
            <th>Product</th>
            <th>Value</th>
            <th>Seller</th>
          </tr>
          {loaded.map((item: any) => {
            return (
              <tr>
                <td>{item.type}</td>
                <td>{item.date}</td>
                <td>{item.product}</td>
                <td>{item.value}</td>
                <td>{item.seller}</td>
              </tr>
            );
          })}
        </table>
      ) : (
        <form>
          <label htmlFor="input-file">Select data file</label>
          <input
            id="input-file"
            type="file"
            accept="text/plain"
            onChange={(e) => handleChange(e.target.files)}
          />
        </form>
      )}
    </div>
  );
}

export default App;
