import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="bg-gray-800 py-2 px-6 mt-4">
      <ul className="flex justify-between items-center">
        <li>
          <Link to="/">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 24 24"
              fill="#fff"
            >
              <path d="M12 0a12 12 0 1 1 0 24 12 12 0 0 1 0-24zm0 5c-3.87 0-7 2.9-7 6.48a6.3 6.3 0 0 0 2.6 5.05V19l2.4-1.3c.63.17 1.3.26 2 .26 3.87 0 7-2.9 7-6.48C19 7.9 15.87 5 12 5zm4.52 4.67l-3.82 4.06-1.79-1.9-3.48 1.9 3.83-4.06 1.83 1.9 3.43-1.9z" />
            </svg>
          </Link>
        </li>
        <li>
          <span className="text-white font-medium">App Copyright 2024</span>
        </li>
      </ul>
    </footer>
  );
}
