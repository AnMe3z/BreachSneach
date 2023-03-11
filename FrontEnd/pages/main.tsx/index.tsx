import React from "react";
import Link from "next/link";
import Head from "next/head";

const SelectProjectType: React.FC = () => {
  async function callServer(event: React.ChangeEvent<HTMLSelectElement>) {
    const selectedValue = event.target.value;
    console.log(`Selected project type: ${selectedValue}`);
    const textBox = document.getElementById("my-textbox") as HTMLTextAreaElement;
    const res = await fetch(`/api/api_base?name1=${selectedValue}`);
    const json = await res.json();
//    const jsonString = JSON.stringify(json.projectType);
    textBox.value = `You have selected ${json.projectType} as your project type.`;
  }

  return (
    <div>
      <Head>
        <title>BreachSneach - Select Project Type</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header>
        <nav>
          <button className="hustle-button">BreachSneach</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">About us</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">Why AI?</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">Stay Informed</button>
          <button className="hustle-button-empty">AAAA</button>
          <button className="hustle-button">Donate</button>
        </nav>
      </header>

      <main>
        <h1 className="title-text">Type</h1>

        <div className="container">
          <h1>Select the type of project </h1>
          
        </div>

        <div className="subtitle-title-text"><select
            name="project-type"
            className="project-type"
            onChange={callServer}
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
        </div>

        <div className="container-two">
          <textarea className="hustle-area" id="my-textbox" readOnly></textarea>
        </div>

          {/* --- show user balance  */}
          {/* // <section>
          //   <NativeCurrencyBalance />

          //   <TokenBalance tokenAddress={ALBT_TOKEN_ADDRESS} symbol="ALBT" />
          //   <USLibrary contractAddress={US_ELECTION_ADDRESS} />
          // </section> */} 
      </main>

      <style jsx>{`

        hustle-area {
          border: 10px solid red;
          outline: none;
        }

        nav {
          display: flex;
          padding: 10px;
          justify-content: space-between;
          align-items: center;
          background-color: black;

          // display: flex;
          // justify-content: space-between;
        }

        main {
          padding: 10px;
          text-align: center;
          background-image: url('https://raw.githubusercontent.com/TariCAD-sistema/BreachSneach/hustle/FrontEnd/images/bg1-gc-bl.jpeg');
          background-repeat: no-repeat;
          background-attachment: fixed;
          background-size: cover;
        }
        
        .container {
          border: 5px solid white;
          background-color: black;
          color: white;
          padding: 16px;
          align: center;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 800px;
          height: 100px;
          margin: auto;
          width: 40%;
        }
        
        p {
          margin: 0;
        }

        .title-text {
          color: white;
          font-weight:bold;
          background-color: black;
          color: white;
          padding: 16px;
          align: center;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100px;
          margin: auto;
          width: 40%;
        }

        .subtitle-title-text {
          color: white;
          font-weight:bold;
          background-color: white;
          color: black;
          padding: 16px;
          align: center;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 50px;
          margin: auto;
          width: 40%;
        }

        .container-two {
          border: 5px solid white;
          background-color: black;
          color: white;
          padding: 16px;
          align: center;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 286px;
          margin: auto;
          width: 40%;
        }


        .text {
          color: white;
        }

        .small-text {
          font-weight: 400;
          color: white;
          // background-color: black;
        }

        .hustle-button {
          padding: .75rem 1.25rem;
          // font-family: "Sono";
          font-size: large; 
          background-color: black;
          color: white;
          font-weight: 700;
          text-transform: uppercase;
          // border-radius: 0.5rem;
          border-color: white;
          border-width: medium;
        }

        .hustle-button-empty {
          padding: .75rem 1.25rem;
          // font-family: "Sono";
          font-size: large; 
          background-color: black;
          color: black;
          font-weight: 700;
          text-transform: uppercase;
          // border-radius: 0.5rem;
          border-color: black;
          border-width: medium;
        }
      `}</style>
    </div>
  );
};

export default SelectProjectType;
