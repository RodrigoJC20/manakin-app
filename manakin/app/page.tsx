import Image from "next/image";

export default function Home() {
  return (
    <main
      className="flex flex-col items-center justify-between p-24"
      style={{
        minHeight: '350vh', // 3 times the screen height
        backgroundImage: 'url(img/bg.png)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      {/* <h1 className="text-4xl font-bold">Welcome to Manakin</h1> */}
      <div className="flex flex-col items-center">
        <button
          className="absolute left-0 button text-black text-xl"
        >yes you</button>
        <button
          className="button text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2"
          style={{
            height: '340px',
            width: '840px',
            position: 'absolute',
            left: '100px',
            bottom: '-1580px',
            backgroundImage: 'url(img/button1.png)',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        ></button>
        <button
          className="button"
          style={{
            height: '330px',
            width: '870px',
            position: 'absolute',
            left: '450px',
            bottom: '-1880px',
            backgroundImage: 'url(img/button2.png)',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        ></button>
      </div>
      <div className="flex flex-col items-center">
      </div>
    </main>
  )
}
