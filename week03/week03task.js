const spotTemplate = document.querySelector("#spot-temp");
const spotSection = document.querySelector(".spot-section");
const promoTemplate = document.querySelector("#promo-temp");
const promoSection = document.querySelector(".promo-section");
let count = 0;
function loadSpots(data) {
  for (let i = count; i - count < 10; i++) {
    if (i < data.length - 3) {
      const spot = spotTemplate.content.cloneNode(true).children[0];
      const title = spot.querySelector(".title");
      let imgUrl = "https" + data[i + 3]["filelist"].split("https")[1];
      spot.style.backgroundImage = `url(${imgUrl})`;
      title.textContent = data[i + 3]["stitle"];
      spotSection.append(spot);
      if (i % 5 == 0) {
        spot.classList.add("wide-block");
      }
    }
  }
  count += 10;
}
fetch(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
)
  .then((response) => {
    if (!response.ok) {
      throw new Error("連線失敗");
    }
    return response.json();
  })
  .then((data) => {
    data = data["data"]["results"];
    for (let i = 0; i < 3; i++) {
      const promo = promoTemplate.content.cloneNode(true).children[0];
      const promoTitle = promo.querySelector(".promo-title");
      const img = promo.querySelector(".promo-img");
      let imgUrl = "https" + data[i]["filelist"].split("https")[1];
      promoTitle.textContent = data[i]["stitle"];
      img.setAttribute("src", imgUrl);
      promoSection.append(promo);
      promo.classList.add(`promo${i + 1}`);
    }

    loadSpots(data);
  })
  .catch((error) => {
    console.error("抓取資料時發生錯誤", error);
  });

function renderSpots() {
  fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("連線失敗");
      }
      return response.json();
    })
    .then((data) => {
      data = data["data"]["results"];
      loadSpots(data);
    })
    .catch((error) => {
      console.error("抓取資料時發生錯誤", error);
    });
}
