import Header from "../components/Header";
import Project from "../components/Project";
import Pagination from "../components/Pagination";
import Footer from "../components/Footer";

export default function Page() {
  return (
    <div>
      <Header></Header>
      <div className="mx-auto max-w-7xl px-8">
        <div className="mx-auto max-w-2xl max-w-none py-8">
          <h2 className="text-2xl font-montserrat font-bold text-gray-900 border-b-2 py-2">
            Project #124
          </h2>
          <Project></Project>
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
}
