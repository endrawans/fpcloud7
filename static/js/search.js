// static/js/search.js
document.addEventListener("DOMContentLoaded", function () {
  const dataProduk = [
    {
      nama: "Free Fire",
      link: "/free fire",
    },
    { nama: "Mobile Legends", link: "/mlbb" },
    { nama: "Valorant", link: "/Valorant" },
    { nama: "Call of Dutty Mobile", link: "/Call of Dutty Mobile" },
    { nama: "PUBG", link: "/PUBG" },
    { nama: "Genshin Impact", link: "/Genshin Impact" },
    { nama: "VIU", link: "#harga-viu" },
    { nama: "Video", link: "#harga-vidio" },
    { nama: "NimoTV", link: "#harga-NimoTV" },
    { nama: "Vision Plus", link: "#harga-VisionPlus" },
  ];

  const searchInput = document.getElementById("searchInput");
  const suggestions = document.getElementById("searchSuggestions");
  const searchSubmit = document.getElementById("searchSubmit");

  // Menampilkan rekomendasi saat mengetik
  searchInput.addEventListener("input", function () {
    const query = searchInput.value.toLowerCase();
    suggestions.innerHTML = ""; // Bersihkan saran sebelumnya
    if (query) {
      const filteredData = dataProduk.filter((item) =>
        item.nama.toLowerCase().includes(query)
      );
      filteredData.forEach((item) => {
        const suggestionItem = document.createElement("div");
        suggestionItem.textContent = item.nama;
        suggestionItem.classList.add("suggestion-item"); // Tambahkan class untuk styling
        suggestionItem.addEventListener("click", () => {
          window.location.href = item.link;
        });
        suggestions.appendChild(suggestionItem);
      });
    }
  });

  // Arahkan ke halaman yang sesuai saat submit
  searchSubmit.addEventListener("click", function () {
    const query = searchInput.value.toLowerCase();
    const result = dataProduk.find((item) =>
      item.nama.toLowerCase().includes(query)
    );
    if (result) {
      window.location.href = result.link;
    } else {
      alert("Produk tidak ditemukan!");
    }
  });
});
