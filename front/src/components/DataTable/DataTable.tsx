import React from "react";
import "./DataTable.css";

interface DataTableProps {
  data: [];
}

function DataTable({ data }: DataTableProps) {
  return (
    <>
      <table>
        <tr>
          <th>Type</th>
          <th>Date</th>
          <th>Product</th>
          <th>Value</th>
          <th>Seller</th>
        </tr>
        {data.map((item: any) => {
          return (
            <tr>
              <td>{item.type}</td>
              <td>{new Date(item.date).toLocaleString()}</td>
              <td>{item.product}</td>
              <td>
                {Intl.NumberFormat("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                }).format(item.value)}
              </td>
              <td>{item.seller}</td>
            </tr>
          );
        })}
      </table>
      <p>
        Total:{" "}
        {Intl.NumberFormat("pt-BR", {
          style: "currency",
          currency: "BRL",
        }).format(
          data.reduce(
            (accumulator, currentValue: any) =>
              accumulator + currentValue.value,
            0
          )
        )}
      </p>
    </>
  );
}

export default DataTable;
