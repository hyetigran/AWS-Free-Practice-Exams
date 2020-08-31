import React, { useEffect } from "react";
import { render } from "react-dom";

function App(props) {
  useEffect(() => {});
  return (
    <div className="App">
      <p>from react</p>
    </div>
  );
}

export default App;

const container = document.getElementById("root");
render(<App />, container);
