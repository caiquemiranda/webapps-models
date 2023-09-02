import { useEffect, useState } from 'react';

function Home() {
    const [financeData, setFinanceData] = useState({});

    useEffect(() => {
        // Fazer uma chamada para a API Python aqui e definir os dados em 'financeData'
    }, []);

    return (
        <div>
            <header className="bg-blue-500 p-4">
                <h1 className="text-white text-3xl font-bold">Meu Website de Finanças</h1>
            </header>

            <main className="container mx-auto mt-4 p-4">
                {/* Renderize os dados financeiros aqui */}
            </main>
        </div>
    );
}

export default Home;
