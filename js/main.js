/**
 * Arpita Sharma Portfolio
 * Minimalist, resilient JavaScript for smooth interactions
 */

document.addEventListener("DOMContentLoaded", () => {
  // --- Mobile Drawer Navigation ---
  const mobileToggle = document.getElementById("mobile-toggle");
  const mobileDrawer = document.getElementById("mobile-drawer");
  const drawerClose = document.getElementById("drawer-close");
  const backdrop = document.getElementById("drawer-backdrop");

  function openDrawer() {
    if (mobileDrawer && backdrop) {
      mobileDrawer.classList.add("open");
      backdrop.classList.add("show");
      document.body.style.overflow = "hidden";
    }
  }

  function closeDrawer() {
    if (mobileDrawer && backdrop) {
      mobileDrawer.classList.remove("open");
      backdrop.classList.remove("show");
      document.body.style.overflow = "";
    }
  }

  if (mobileToggle) mobileToggle.addEventListener("click", openDrawer);
  if (drawerClose) drawerClose.addEventListener("click", closeDrawer);
  if (backdrop) backdrop.addEventListener("click", closeDrawer);

  document.querySelectorAll(".drawer-links-list a").forEach(link => {
    link.addEventListener("click", closeDrawer);
  });

  // --- Scroll Spy & Navigation Highlight ---
  const sections = document.querySelectorAll("section[id], main[id]");
  const navLinks = document.querySelectorAll(".nav-menu .nav-item-link");
  const backToTopBtn = document.getElementById("back-to-top");

  function handleScroll() {
    const scrollPos = window.scrollY + 120;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute("id");

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(link => {
          link.classList.remove("active");
          if (link.getAttribute("href") === `#${id}`) {
            link.classList.add("active");
          }
        });
      }
    });

    if (backToTopBtn) {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add("visible");
      } else {
        backToTopBtn.classList.remove("visible");
      }
    }
  }

  window.addEventListener("scroll", handleScroll, { passive: true });

  if (backToTopBtn) {
    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Escape key closes mobile drawer
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeDrawer();
    }
  });

  // --- Copy to Clipboard Buttons ---
  document.querySelectorAll(".copy-button").forEach(btn => {
    btn.addEventListener("click", async () => {
      const textToCopy = btn.getAttribute("data-copy");
      if (!textToCopy) return;

      try {
        await navigator.clipboard.writeText(textToCopy);
        const originalHtml = btn.innerHTML;
        btn.innerHTML = `
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span style="color: #059669;">Copied</span>
        `;
        showToast(`Copied "${textToCopy}" to clipboard`);
        setTimeout(() => {
          btn.innerHTML = originalHtml;
        }, 2000);
      } catch (err) {
        showToast("Failed to copy automatically.");
      }
    });
  });



  // --- Toast Notice ---
  let toastTimer;
  function showToast(message) {
    const toast = document.getElementById("toast");
    if (!toast) return;

    toast.textContent = message;
    toast.classList.add("show");

    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove("show");
    }, 2800);
  }
});
