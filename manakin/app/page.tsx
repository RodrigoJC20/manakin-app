import Image from 'next/image'

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
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Upload wooo
        </button>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Upload background
        </button>
      </div>
    </main>
  )
}
