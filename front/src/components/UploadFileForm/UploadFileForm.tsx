import React, { useState } from "react";
import './UploadFileForm.css'

interface UploadFileFormProps {
  handleChange: (e: FileList) => void;
}

function UploadFileForm({ handleChange }: UploadFileFormProps) {
  return (
    <form>
      <label htmlFor="input-file">Select data file</label>
      <input
        id="input-file"
        type="file"
        accept="text/plain"
        onChange={(e) => e.target.files && handleChange(e.target.files)}
      />
    </form>
  );
}

export default UploadFileForm;
