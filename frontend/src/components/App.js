import React, { useEffect } from "react";
import { render } from "react-dom";
import { HashRouter as Router, Route, Switch } from "react-router-dom";
import ExamOptions from "./pages/ExamOptions/ExamOptions";
import ExamSessions from "./pages/ExamSessions/ExamSessions";
import ExamReview from "./pages/ExamReview/ExamReview";

//import "bootstrap/dist/css/bootstrap.min.css";

function App(props) {
  useEffect(() => {});
  return (
    <div className="App">
      <Router>
        <div className="container">
          <Switch>
            <Route exact path="/" component={ExamOptions} />
            <Route exact path="/exam-sessions" component={ExamSessions} />
            <Route exact path="/exam-review" component={ExamReview} />
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;

render(<App />, document.getElementById("root"));
