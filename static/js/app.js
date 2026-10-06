document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".zoom-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const box = document.getElementById("lightbox");
      const img = document.getElementById("lightbox-img");
      img.src = btn.dataset.src;
      box.classList.add("open");
      box.setAttribute("aria-hidden", "false");
    });
  });
  const close = () => {
    const box = document.getElementById("lightbox");
    if (box) { box.classList.remove("open"); box.setAttribute("aria-hidden", "true"); }
  };
  document.querySelector(".lightbox-close")?.addEventListener("click", close);
  document.getElementById("lightbox")?.addEventListener("click", e => {
    if (e.target.id === "lightbox") close();
  });
  document.addEventListener("keydown", e => { if (e.key === "Escape") close(); });

  // Small floating-heart effect on the landing page.
  if (location.pathname.includes("/page/0")) {
    setInterval(() => {
      const h = document.createElement("span");
      h.textContent = ["♥","♡","✦","✧"][Math.floor(Math.random()*4)];
      h.style.cssText = `position:fixed;left:${Math.random()*100}vw;bottom:-20px;z-index:2;color:#ff63c0;font-size:${10+Math.random()*15}px;pointer-events:none;animation:floatHeart 4s linear forwards;opacity:.75`;
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 4100);
    }, 900);
    const style = document.createElement("style");
    style.textContent = "@keyframes floatHeart{to{transform:translateY(-105vh) rotate(240deg);opacity:0}}";
    document.head.appendChild(style);
  }
});