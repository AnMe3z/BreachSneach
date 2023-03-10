import React from "react";

const SelectProjectType: React.FC = () => {
  const handleSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedValue = event.target.value;
    console.log(`Selected project type: ${selectedValue}`);
    const textBox = document.getElementById("my-textbox") as HTMLTextAreaElement;
    textBox.value = `You have selected "${selectedValue}" as your project type.`;
  };

  return (
    <html>
      <head>
        <meta charSet="UTF-8" />
        <title>Select Project Type</title>
        <link rel="icon" href="/favicon.ico" />
        <style>
          {`
            body {
              display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: flex-start;
              height: 100vh;
              margin: 0;
            }

            h1 {
              font-size: 2.5rem;
              margin-bottom: 2rem;
            }

            .project-type {
              padding: 1rem 2rem;
              font-size: 1.2rem;
              background-color: #000000;
              color: #fff;
              border: none;
              border-radius: 0.25rem;
              cursor: pointer;
            }

            .project-type:hover {
              background-color: #32127A;
            }

            div {
              margin-top: 3rem;
              text-align: center;
            }

            textarea {
              width: 100%;
              height: 50vh;
              margin-top: 3rem;
              font-size: 1.2rem;
              padding: 1rem;
              box-sizing: border-box;
              border: 2px solid #32127A;
              resize:none;
            }
          `}
        </style>
      </head>
      <body>
        <div>
          <h1>Select the type of project you want to start</h1>
          <select
            name="project-type"
            className="project-type"
            onChange={handleSelect}
          >
            <option value="Hospital">Hospital</option>
            <option value="Bank">Bank</option>
            <option value="Supermarket">Supermarket</option>
            <option value="Hardware Store">Hardware Store</option>
            <option value="School">School</option>
            <option value="Shooting Range">Shooting Range</option>
            <option value="Kindergarten">Kindergarten</option>
            <option value="Government">Government</option>
            <option value="Non-Profit">Non-Profit</option>
            <option value="Train Station">Train Station</option>
            <option value="Small project">Small project</option>
            <option value="Local Shop">Local Shop</option>
            <option value="Pizzeria">Pizzeria</option>
            <option value="Sandwich Shop">Sandwich Shop</option>
            <option value="Burger Franchise">Burger Franchise</option>
          </select>
          <textarea id="my-textbox" readOnly></textarea>
        </div>
      </body>
    </html>
  );
};

export default SelectProjectType;
