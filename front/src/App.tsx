import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import UploadFormFile from "./components/UploadFileForm/UploadFileForm";
import DataTable from "./components/DataTable/DataTable";
import Loading from "./components/Loading/Loading";
import Alert from "./components/Alert/Alert";

const API_URL = "http://0.0.0.0:8000";

function App() {
  const [data, setData] = useState<[]>([]);
  const [loading, setLoading] = useState(false);
  const [showAlert, setShowAlert] = useState({ show: false, message: "" });

  const handleChange = (fileInput: FileList) => {
    const file = fileInput[0];
    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    fetch(API_URL + "/product/file", {
      method: "POST",
      body: formData,
    })
      .then(async (response) => {
        if (response.ok) {
          response.json().then((data) => {
            console.log(data);
            setData(data);
            setLoading(false);
            setShowAlert({ show: true, message: "File Loaded" });
          });
        } else {
          setShowAlert({
            show: true,
            message: await response.json().then((data) => data.detail),
          });
          setLoading(false);
        }
      })
      .catch((error: Error) => {
        setShowAlert({ show: true, message: error.message });
        setLoading(false);
      });
  };

  return (
    <div className="App">
      {loading && <Loading />}
      {data && data.length > 0 ? (
        <div className="Table">
          <DataTable data={data} />
          <button onClick={() => setData([])}>RETORNAR</button>
        </div>
      ) : (
        <UploadFormFile handleChange={handleChange} />
      )}
      {showAlert.show && (
        <Alert setShowAlert={setShowAlert}>{showAlert.message}</Alert>
      )}
    </div>
  );
}

export default App;
