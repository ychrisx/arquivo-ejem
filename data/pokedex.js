async function buscarPokemon() {
    const nome = document.getElementById("pokemonInput").value.toLowerCase();

    try {
        const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${nome}`);
        const data = await res.json();

        const speciesRes = await fetch(data.species.url);
        const speciesData = await speciesRes.json();

        const nomePokemon = data.name;
        const numero = data.id;
        const tipo = data.types.map(t => t.type.name).join(", ");
        const sprite = data.sprites.front_default;

        const descricao = speciesData.flavor_text_entries.find(
            entry => entry.language.name === "en"
        ).flavor_text.replace(/\f/g, " ");

        document.getElementById("nome").innerText = nomePokemon.toUpperCase();

        document.getElementById("infoTop").innerHTML = `
            Nº: ${numero}<br>
            Tipo: ${tipo}
        `;

        document.getElementById("infoBottom").innerText = descricao;

        const img = document.getElementById("sprite");
        img.src = sprite;

        img.classList.remove("jump");
        void img.offsetWidth;
        img.classList.add("jump");

        const audio = document.getElementById("cry");
        audio.src = `https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/${numero}.ogg`;
        audio.play();

    } catch {
        alert("Pokémon não encontrado!");
    }
}
