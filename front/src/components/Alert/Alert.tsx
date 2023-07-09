import React, { ReactNode, useEffect, useState } from "react";
import { FaTimes as CloseIcon } from "react-icons/fa";
import "./Alert.css";

interface ToastProps {
  children: ReactNode;
  setShowAlert: ({}: any) => void;
}

function Toast({ children, setShowAlert }: ToastProps) {
  return (
    <span>
      <div className="toast">
        {children}
        <CloseIcon onClick={() => setShowAlert({ show: false, message: "" })} />
      </div>
    </span>
  );
}

export default Toast;
