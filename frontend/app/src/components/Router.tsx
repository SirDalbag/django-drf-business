import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Project from "../pages/Project";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"*"} element={<Home />}></Route>
        <Route path={""} element={<Home />}></Route>
        <Route path={"project"} element={<Project />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
