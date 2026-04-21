import { useState } from "react";

export default function App() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);

  const upload = async () => {
    if (!file) return;

    const form = new FormData();
    form.append("file", file);

    const res = await fetch("http://localhost:8000/process", {
      method: "POST",
      body: form,
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>FinMap AI Dashboard</h1>

      <input type="file" onChange={(e) => setFile(e.target.files?.[0] || null)} />
      <button onClick={upload}>Upload</button>

      {result && (
        <>
          <h2>Mapping</h2>

          <table border={1} cellPadding={8}>
            <thead>
              <tr>
                <th>Field</th>
                <th>Column</th>
                <th>Confidence</th>
                <th>Explanation</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(result.mapping).map(([key, val]: any) => (
                <tr key={key}>
                  <td>{key}</td>
                  <td>{val.column}</td>
                  <td>{val.confidence}</td>
                  <td>{val.explanation}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <h3>Missing Fields</h3>
          <pre>{JSON.stringify(result.missing_fields, null, 2)}</pre>

          <h3>Unmapped Columns</h3>
          <pre>{JSON.stringify(result.unmapped_columns, null, 2)}</pre>
        </>
      )}
    </div>
  );
}