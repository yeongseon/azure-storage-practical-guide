(() => {
  const OVERLAY_ID = "mermaid-zoom-overlay";

  const destroyOverlay = () => {
    const overlay = document.getElementById(OVERLAY_ID);
    if (overlay) {
      overlay.classList.add("mermaid-zoom-fade-out");
      setTimeout(() => {
        overlay.parentNode?.removeChild(overlay);
      }, 200);
    }
    document.removeEventListener("keydown", onKeyDown);
  };

  const createOverlay = () => {
    const overlay = document.createElement("div");
    overlay.id = OVERLAY_ID;

    const closeBtn = document.createElement("button");
    closeBtn.className = "mermaid-zoom-close";
    closeBtn.innerHTML = "&times;";
    closeBtn.setAttribute("aria-label", "Close");
    closeBtn.addEventListener("click", destroyOverlay);

    const hint = document.createElement("div");
    hint.className = "mermaid-zoom-hint";
    hint.textContent = "Scroll to zoom \u00b7 Drag to pan \u00b7 Esc to close";

    const container = document.createElement("div");
    container.className = "mermaid-zoom-container";

    overlay.append(closeBtn, hint, container);
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) destroyOverlay();
    });

    return { overlay, container };
  };

  const onKeyDown = (e) => {
    if (e.key === "Escape") destroyOverlay();
  };

  const enablePanZoom = (container, svgEl) => {
    let scale = 1;
    let panX = 0;
    let panY = 0;
    let isPanning = false;
    let startX = 0;
    let startY = 0;
    let lastTouchDist = 0;

    const applyTransform = () => {
      svgEl.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
    };

    container.addEventListener(
      "wheel",
      (e) => {
        e.preventDefault();
        const delta = e.deltaY > 0 ? -0.1 : 0.1;
        scale = Math.min(Math.max(0.3, scale + delta), 5);
        applyTransform();
      },
      { passive: false }
    );

    container.addEventListener("mousedown", (e) => {
      isPanning = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
      container.style.cursor = "grabbing";
      e.preventDefault();
    });

    document.addEventListener("mousemove", (e) => {
      if (!isPanning) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      applyTransform();
    });

    document.addEventListener("mouseup", () => {
      isPanning = false;
      container.style.cursor = "grab";
    });

    container.addEventListener(
      "touchstart",
      (e) => {
        if (e.touches.length === 1) {
          isPanning = true;
          startX = e.touches[0].clientX - panX;
          startY = e.touches[0].clientY - panY;
        } else if (e.touches.length === 2) {
          isPanning = false;
          lastTouchDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
        }
      },
      { passive: true }
    );

    container.addEventListener(
      "touchmove",
      (e) => {
        if (e.touches.length === 1 && isPanning) {
          panX = e.touches[0].clientX - startX;
          panY = e.touches[0].clientY - startY;
          applyTransform();
        } else if (e.touches.length === 2) {
          const dist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          if (lastTouchDist > 0) {
            scale = Math.min(Math.max(0.3, scale * (dist / lastTouchDist)), 5);
            applyTransform();
          }
          lastTouchDist = dist;
        }
      },
      { passive: true }
    );

    container.addEventListener("touchend", () => {
      isPanning = false;
      lastTouchDist = 0;
    });
  };

  const openDiagram = (mermaidEl) => {
    const existing = document.getElementById(OVERLAY_ID);
    existing?.parentNode?.removeChild(existing);

    const parts = createOverlay();
    const svgSource = mermaidEl.querySelector("svg");
    if (!svgSource) return;

    const svgClone = svgSource.cloneNode(true);
    svgClone.style.maxWidth = "none";
    svgClone.style.maxHeight = "none";
    svgClone.style.width = "auto";
    svgClone.style.height = "auto";
    svgClone.style.transformOrigin = "center center";
    svgClone.style.transition = "transform 0.1s ease-out";
    svgClone.style.cursor = "grab";

    parts.container.appendChild(svgClone);
    document.body.appendChild(parts.overlay);

    requestAnimationFrame(() => {
      parts.overlay.classList.add("mermaid-zoom-visible");
    });

    enablePanZoom(parts.container, svgClone);
    document.addEventListener("keydown", onKeyDown);
  };

  const init = () => {
    document.addEventListener("click", (e) => {
      const mermaidEl = e.target.closest(".mermaid");
      if (mermaidEl?.querySelector("svg")) {
        openDiagram(mermaidEl);
      }
    });

    const style = document.createElement("style");
    style.textContent = ".mermaid { cursor: pointer; }";
    document.head.appendChild(style);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
