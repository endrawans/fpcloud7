const slides = document.querySelectorAll(".slides .slide"); // Ambil semua slide
const totalSlides = slides.length;
let currentIndex = 0; // Index slide aktif
const slideInterval = 5000; // Delay waktu antar slide (5 detik)
let autoSlide; // Variabel untuk interval otomatis

// Fungsi untuk pindah ke slide tertentu
function showSlide(index) {
  // Validasi index agar loop dari awal atau akhir
  if (index < 0) {
    currentIndex = totalSlides - 1; // Kembali ke slide terakhir
  } else if (index >= totalSlides) {
    currentIndex = 0; // Kembali ke slide pertama
  } else {
    currentIndex = index;
  }

  // Geser slide dengan transform translateX
  document.getElementById("slides").style.transform = `translateX(-${
    currentIndex * 100
  }%)`;
}

// Fungsi slide otomatis
function startAutoSlide() {
  autoSlide = setInterval(() => {
    nextSlide();
  }, slideInterval);
}

// Fungsi tombol navigasi manual
function nextSlide() {
  showSlide(currentIndex + 1);
}

function prevSlide() {
  showSlide(currentIndex - 1);
}

// Hentikan auto-slide saat tombol ditekan, lalu mulai lagi
function resetAutoSlide() {
  clearInterval(autoSlide);
  startAutoSlide();
}

// Mulai slider
startAutoSlide();

// Event listener untuk tombol
document.querySelector(".prev").addEventListener("click", resetAutoSlide);
document.querySelector(".next").addEventListener("click", resetAutoSlide);
