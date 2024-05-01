import { Fragment } from "react";
import { Link } from "react-router-dom";
import { Menu, Transition } from "@headlessui/react";

const user = {
  firstName: "John",
  lastName: "Doe",
  avatar:
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
const navigation = [
  { name: "Dashboard", href: "#" },
  { name: "Team", href: "#" },
  { name: "Projects", href: "#" },
  { name: "Calendar", href: "#" },
  { name: "Reports", href: "#" },
];

export default function Header() {
  return (
    <header className="bg-gray-800 py-2 px-6">
      <div className="flex justify-between items-center ">
        <ul className="flex items-center gap-4">
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
          {navigation.map((item, index) => (
            <li
              key={index}
              className="text-white font-montserrat font-medium rounded-md p-2 hover:bg-gray-700"
            >
              <Link to={item.href}>{item.name}</Link>
            </li>
          ))}
        </ul>
        <Menu as="div" className="relative ml-3">
          <div>
            <Menu.Button className="relative flex max-w-xs items-center rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
              <span className="absolute -inset-1.5" />
              <img className="h-8 w-8 rounded-full" src={user.avatar} />
            </Menu.Button>
          </div>
          <Transition
            as={Fragment}
            enter="transition ease-out duration-100"
            enterFrom="transform opacity-0 scale-95"
            enterTo="transform opacity-100 scale-100"
            leave="transition ease-in duration-75"
            leaveFrom="transform opacity-100 scale-100"
            leaveTo="transform opacity-0 scale-95"
          >
            <Menu.Items className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
              <Menu.Item>
                <Link
                  to="sign-out"
                  className="block px-4 py-2 text-sm text-gray-600 font-montserrat hover:text-gray-900"
                >
                  Sign Out
                </Link>
              </Menu.Item>
            </Menu.Items>
          </Transition>
        </Menu>
      </div>
    </header>
  );
}
