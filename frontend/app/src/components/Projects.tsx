import { Link } from "react-router-dom";

const callouts = [
  {
    name: "Desk and Office",
    description: "Work from home accessories",
    image:
      "https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg",
    imageAlt:
      "Desk with leather desk pad, walnut desk organizer, wireless keyboard and mouse, and porcelain mug.",
    href: "#",
  },
  {
    name: "Self-Improvement",
    description: "Journals and note-taking",
    image:
      "https://tailwindui.com/img/ecommerce-images/home-page-02-edition-02.jpg",
    imageAlt:
      "Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant.",
    href: "#",
  },
  {
    name: "Travel",
    description: "Daily commute essentials",
    image:
      "https://tailwindui.com/img/ecommerce-images/home-page-02-edition-03.jpg",
    imageAlt: "Collection of four insulated travel bottles on wooden shelf.",
    href: "#",
  },
  {
    name: "Desk and Office",
    description: "Work from home accessories",
    image:
      "https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg",
    imageAlt:
      "Desk with leather desk pad, walnut desk organizer, wireless keyboard and mouse, and porcelain mug.",
    href: "#",
  },
  {
    name: "Self-Improvement",
    description: "Journals and note-taking",
    image:
      "https://tailwindui.com/img/ecommerce-images/home-page-02-edition-02.jpg",
    imageAlt:
      "Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant.",
    href: "#",
  },
  {
    name: "Travel",
    description: "Daily commute essentials",
    image:
      "https://tailwindui.com/img/ecommerce-images/home-page-02-edition-03.jpg",
    href: "#",
  },
];

export default function Projects() {
  return (
    <div className="mt-6 grid grid-cols-3 gap-x-6 gap-y-6 space-y-0">
      {callouts.map((callout, index) => (
        <div key={index} className="group relative">
          <div className="relative h-80 w-full overflow-hidden rounded-lg bg-white sm:aspect-h-1 sm:aspect-w-2 lg:aspect-h-1 lg:aspect-w-1 group-hover:opacity-75 sm:h-64">
            <img
              src={callout.image}
              className="h-full w-full object-cover object-center"
            />
          </div>
          <h3 className="mt-6 font-montserrat text-sm text-gray-500">
            <Link to={callout.href}>
              <span className="absolute inset-0" />
              {callout.name}
            </Link>
          </h3>
          <p className="text-base font-montserrat font-semibold text-gray-900">
            {callout.description}
          </p>
        </div>
      ))}
    </div>
  );
}
