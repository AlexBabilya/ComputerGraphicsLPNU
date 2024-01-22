var imageLoader = document.getElementById('imageUpload');
var canvasimgBefore = document.getElementById('img-rgb');
var ctxImgBefore = canvasimgBefore.getContext('2d', { willReadFrequently: true });
// var overlayCanvas1 = document.getElementById('overlay1');
// var ctxOverlay1 = overlayCanvas1.getContext('2d', { willReadFrequently: true });

var canvasimgAfter = document.getElementById('img-hsv');
var ctxImgAfter = canvasimgAfter.getContext('2d', { willReadFrequently: true });


var canvasimgSaturation = document.getElementById('img-saturation');
var ctxImgSaturation = canvasimgSaturation.getContext('2d', { willReadFrequently: true });

var saturationSlider = document.getElementById('saturation');
var lightnessSlider = document.getElementById('lightness');

let selectedWidth = canvasimgAfter.width;
let selectedHeight = canvasimgAfter.height;

let width = canvasimgAfter.width;
let height = canvasimgAfter.height;

//document.getElementById("overlay3").style.pointerEvents = 'none';

function displayPixelColor(x, y, ctx) {
    // Округлення координат до найближчого цілого числа
    x = Math.round(x);
    y = Math.round(y);
    console.log(x, " ", y)
    // Отримання даних про піксель
    var pixel = ctx.getImageData(x, y, 1, 1).data;
    // Встановлення кольору для елемента color-display
    var colorDisplay = document.getElementById('color-display');
    colorDisplay.style.backgroundColor = `rgb(${pixel[0]}, ${pixel[1]}, ${pixel[2]})`;

    var red = pixel[0];     
    var green = pixel[1];
    var blue = pixel[2]; 

    var hsvColor = rgbToHsv(red, green, blue);
    document.getElementById("h-value").value = Math.round(hsvColor[0]);
    document.getElementById("s-value").value = Math.round(hsvColor[1]);
    document.getElementById("v-value").value = Math.round(hsvColor[2]);

    document.getElementById("r-value").value = Math.round(red);
    document.getElementById("g-value").value = Math.round(green);
    document.getElementById("b-value").value = Math.round(blue);
}


function rgbToHsv(r, g, b) {
    // Ділимо значення R, G, B на 255
    r /= 255;
    g /= 255;
    b /= 255;

    // Обчислюємо cmax (максимальне з трьох значень), cmin (мінімальне з трьох значень) та різницю між ними
    var cmax = Math.max(r, g, b);
    var cmin = Math.min(r, g, b);
    var diff = cmax - cmin;
    var h = 0; // Відтінок
    var s = 0; // Насиченість

    // Обчислення відтінку (Hue)
    if (diff === 0) {
        h = 0; // Якщо різниця 0, відтінок буде 0 (відтінок не визначено)
    } else if (cmax === r) {
        h = (60 * ((g - b) / diff) + 360) % 360;
    } else if (cmax === g) {
        h = (60 * ((b - r) / diff) + 180) % 360;
    } else if (cmax === b) {
        h = (60 * ((r - g) / diff) + 240) % 360;
    }

    // Обчислення насиченості (Saturation)
    if (cmax === 0) {
        s = 0; // Якщо cmax 0, то насиченість 0 (абсолютно ненасичений колір)
    } else {
        s = (diff / cmax) * 100;
    }

    // Обчислення значення (Value)
    var v = cmax * 100;
    // Повертаємо результати у форматі HSV
    return [h, s, v];
}

function hsvToRgb(h, s, v) {
    // Перевірка на вхідні значення h, s, v (в діапазоні [0, 360], [0, 100], [0, 100])
    h = (h % 360 + 360) % 360; // Гарантуємо, що h знаходиться у діапазоні [0, 360]
    s = Math.min(100, Math.max(0, s)); // Обмежуємо s в діапазоні [0, 100]
    v = Math.min(100, Math.max(0, v)); // Обмежуємо v в діапазоні [0, 100]

    // Нормалізуємо значення s та v до діапазону [0, 1]
    s /= 100;
    v /= 100;

    var c = v * s; // Обчислюємо Chroma (насиченість), яка показує, наскільки сильним є колір
    var x = c * (1 - Math.abs((h / 60) % 2 - 1)); // Обчислюємо x
    var m = v - c; // Обчислюємо зсув яскравості (це кількість білого кольору, яку потрібно додати, щоб отримати потрібну яскравість)

    var r, g, b;

    // Визначаємо, в якому секторі кольорового колеса перебуваємо та обчислюємо значення R, G і B
    if (h >= 0 && h < 60) {
        r = c;
        g = x;
        b = 0;
    } else if (h >= 60 && h < 120) {
        r = x;
        g = c;
        b = 0;
    } else if (h >= 120 && h < 180) {
        r = 0;
        g = c;
        b = x;
    } else if (h >= 180 && h < 240) {
        r = 0;
        g = x;
        b = c;
    } else if (h >= 240 && h < 300) {
        r = x;
        g = 0;
        b = c;
    } else {
        r = c;
        g = 0;
        b = x;
    }

    // Перетворюємо значення R, G і B у діапазон [0, 255] та повертаємо їх у форматі RGB
    r = Math.round((r + m) * 255);
    g = Math.round((g + m) * 255);
    b = Math.round((b + m) * 255);

    return [r, g, b];
}


function handleImage(e) {
    var reader = new FileReader();
    reader.onload = function(event) {
      var img = new Image();
      img.onload = function() {
        lightnessSlider.value = 0;
        saturationSlider.value = 0;
        // Очищення канвасу перед малюванням нового зображення
        ctxImgBefore.clearRect(0, 0, canvasimgBefore.width, canvasimgBefore.height);
        ctxImgAfter.clearRect(0, 0, canvasimgAfter.width, canvasimgAfter.height);
        ctxImgSaturation.clearRect(0, 0, canvasimgSaturation.width, canvasimgSaturation.height);
  
        // Визначення масштабу для збереження пропорцій зображення
        var scaleWidth = canvasimgBefore.width / img.width;
        var scaleHeight = canvasimgBefore.height / img.height;
        var scale = Math.min(scaleWidth, scaleHeight);
        // Обчислення нових розмірів зображення
        var imgWidthScaled = img.width * scale;
        var imgHeightScaled = img.height * scale;
  
        // Обчислення позиції для центрування зображення на канвасі
        var dx = (canvasimgBefore.width - imgWidthScaled) / 2;
        var dy = (canvasimgBefore.height - imgHeightScaled) / 2;
        
        // Малювання зображення на канвасі з центруванням
        ctxImgBefore.drawImage(img, 0, dy, canvasimgBefore.width, imgHeightScaled);

        var convertedCanvas = convertImage(img);
        ctxImgAfter.drawImage(convertedCanvas, 0, dy, canvasimgBefore.width, imgHeightScaled);
        ctxImgSaturation.drawImage(img, 0, dy, canvasimgBefore.width, imgHeightScaled);
        
        selectedPixelsBefore = ctxImgBefore.getImageData(0, 0, selectedWidth, selectedHeight).data;
        selectedPixelsAfter = ctxImgAfter.getImageData(0, 0, selectedWidth, selectedHeight).data;
      };
      img.src = event.target.result;
    };
    reader.readAsDataURL(e.target.files[0]);
}

function convertImage(image) {
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');

    // Задаємо розміри канвасу такі ж, як у зображення
    canvas.width = image.width;
    canvas.height = image.height;

    // Малюємо зображення на канвасі
    ctx.drawImage(image, 0, 0);

    // Отримуємо дані пікселів зображення
    var imageData = ctx.getImageData(0, 0, image.width, image.height);
    var data = imageData.data;

    // Проходимося по кожному пікселю
    for (var i = 0; i < data.length; i += 4) {
        var red = data[i];     
        var green = data[i+1];
        var blue = data[i+2]; 

        var hsv = rgbToHsv(red, green, blue)
        var rgbColor = hsvToRgb(hsv[0], hsv[1], hsv[2])

        data[i] = rgbColor[0];
        data[i+1] = rgbColor[1];
        data[i+2] = rgbColor[2];
    }

    // Повертаємо змінені дані пікселів назад на канвас
    ctx.putImageData(imageData, 0, 0);

    // Повертаємо канвас, а не DataURL
    return canvas;
}

function drawCircleOnOverlay(x, y, overlayCanvas, ctx) {
    // Отримання даних про піксель з оригінального канвасу
    var pixelData = ctx.getImageData(x, y, 1, 1).data;
  
    // Визначення контрастного кольору для обведення
    var contrastColor = (pixelData[0] * 0.299 + pixelData[1] * 0.587 + pixelData[2] * 0.114) > 186 ? 'black' : 'white';
    var ctxOverlay = canvasimgBefore.getContext('2d', { willReadFrequently: true });
    // Очищення другого канвасу
    // ctxOverlay.clearRect(0, 0, overlayCanvas.width, overlayCanvas.height);
  
    // Встановлення кольору і стилю лінії
    ctxOverlay.strokeStyle = contrastColor;
    ctxOverlay.lineWidth = 1;
  
    // Малювання кружечка на другому канвасі
    ctxOverlay.beginPath();
    ctxOverlay.arc(x, y, 5, 0, Math.PI * 2, false);
    ctxOverlay.stroke();
}

function changeSaturation(pixelArray, imgWidth, value) {
    var startX = 0;
    var startY = 0;
    let fragWidth = canvasimgSaturation.width;
    let fragHeight = canvasimgSaturation.height;

    for (let y = startY; y < startY + fragHeight; y++) {
        for (let x = startX; x < startX + fragWidth; x++) {
            let i = (y * imgWidth + x) * 4;
            let red = pixelArray[i];
            let green = pixelArray[i + 1];
            let blue = pixelArray[i + 2];
            
            var hsvColor = rgbToHsv(red, green, blue)

            if (hsvColor[0] > 80 && hsvColor[0] < 160) {
                var rgbColor = hsvToRgb(hsvColor[0], hsvColor[1] + value, hsvColor[2]);

                pixelArray[i] = rgbColor[0];
                pixelArray[i + 1] = rgbColor[1];
                pixelArray[i + 2] = rgbColor[2];
            }
        }
    }
}

  
// overlayCanvas1.addEventListener('mousemove', function(event) {
//     // Визначення позиції курсору відносно канвасу
//     var rect = overlayCanvas1.getBoundingClientRect();
//     var x = event.clientX - rect.left;
//     var y = event.clientY - rect.top;
  
//     drawCircleOnOverlay(Math.round(x), Math.round(y), overlayCanvas1, ctxImgBefore);
//     displayPixelColor(Math.round(x), Math.round(y), ctxImgBefore);
// });


// overlayCanvas1.addEventListener('mousedown', function(event) {
//     document.getElementById("overlay3").style.pointerEvents = 'auto';
// });

canvasimgBefore.addEventListener('mousemove', function(event) {
    // Визначення позиції курсору відносно канвасу
    var rect = canvasimgBefore.getBoundingClientRect();
    var x = event.clientX - rect.left - 50;
    var y = (event.clientY - rect.top) / 3.2;

    // console.log(event.clientX, " | ", event.clientY, " |||| ", rect.left, " | ", rect.top)
    // drawCircleOnOverlay(Math.round(x), Math.round(y), canvasimgBefore, ctxImgAfter);
    displayPixelColor(Math.round(x), Math.round(y), ctxImgAfter );
});

imageLoader.addEventListener('change', handleImage, false);

saturationSlider.addEventListener('input', function() {
    var saturationValue = parseFloat(saturationSlider.value);

    var imageData = ctxImgBefore.getImageData(0, 0, width, height);
    changeSaturation(imageData.data, width, saturationValue);
    ctxImgSaturation.putImageData(imageData, 0, 0);
});


function exportImg() {
    var dataURL = canvasimgBefore.toDataURL("image/png");
    var a = document.createElement('a');
    a.href = dataURL;
    a.download = 'ColoredImage_RGB.jpeg';
    a.click();


    dataURL = canvasimgAfter.toDataURL("image/png");
    a = document.createElement('a');
    a.href = dataURL;
    a.download = 'ColoredImage_HSV.jpeg';
    a.click();


    dataURL = canvasimgSaturation.toDataURL("image/png");
    a = document.createElement('a');
    a.href = dataURL;
    a.download = 'ColoredImage_SATURATED.jpeg';
    a.click();
}

document.getElementById("download-button").addEventListener('click', exportImg);






