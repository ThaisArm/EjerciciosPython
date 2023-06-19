clc, clear, close all

% Leer imagen original
imagen_original = imread('Manzana.jpg');
imagen_gris = rgb2gray(imagen_original);

%FILTRO DE SOBEL
% Sobel horizontal
filtro_sobel_horizontal = [-1, 0, 1; -2, 0, 2; -1, 0, 1];
gradiente_horizontal = imfilter(double(imagen_gris), filtro_sobel_horizontal);
gradiente_horizontal = uint8(abs(gradiente_horizontal));

%Sobel vertical
filtro_sobel_vertical = [-1, -2, -1; 0, 0, 0; 1, 2, 1];
gradiente_vertical = imfilter(double(imagen_gris), filtro_sobel_vertical);
gradiente_vertical = uint8(abs(gradiente_vertical));

% Magnitud del gradiente
magnitud_gradiente = sqrt(double(gradiente_horizontal).^2 + double(gradiente_vertical).^2);
magnitud_gradiente = uint8(magnitud_gradiente);

% Mostrar resultados
figure(1);
subplot(2, 2, 1);
imshow(imagen_gris);
title('Imagen Original en Gris');

subplot(2, 2, 2);
imshow(gradiente_horizontal);
title('Gradiente Horizontal');

subplot(2, 2, 3);
imshow(gradiente_vertical);
title('Gradiente Vertical');

subplot(2, 2, 4);
imshow(magnitud_gradiente);
title('Magnitud del Gradiente');

%FILTRO LAPLACIAN
filteredImg = imfilter(imagen_gris, fspecial('laplacian'));

figure(2);
subplot(1, 2, 1);
imshow(imagen_gris);
title('Imagen Original');
subplot(1, 2, 2);
imshow(filteredImg);
title('Filtro Laplacian');

%FILTRO DE LAPACIAN DE GAUSS
% Aplicar el filtro
filteredImg = imfilter(imagen_gris, fspecial('log'));

% Ajustar la escala
enhancedImg = imadjust(filteredImg);

figure(3);
subplot(1, 3, 1);
imshow(imagen_gris);
title('Imagen Original');
subplot(1, 3, 2);
imshow(filteredImg);
title('Imagen Filtrada');
subplot(1, 3, 3);
imshow(enhancedImg);
title('Imagen Realzada');

%FILTRO DE PREWITT
filteredImg0 = imfilter(imagen_gris, fspecial('prewitt'));
filteredImg45 = imfilter(imagen_gris, fspecial('prewitt'));
filteredImg90 = imfilter(imagen_gris, rot90(fspecial('prewitt')));
filteredImg135 = imfilter(imagen_gris, rot90(fspecial('prewitt'), 2));

finalImg = filteredImg0 + filteredImg45 + filteredImg90 + filteredImg135;

figure(4);
subplot(3, 2, 1);
imshow(filteredImg135);
title('Filtro de Prewitt (135 grados)');
subplot(3, 2, 2);
imshow(filteredImg0);
title('Filtro de Prewitt (0 grados)');
subplot(3, 2, 3);
imshow(filteredImg45);
title('Filtro de Prewitt (45 grados)');
subplot(3, 2, 4);
imshow(filteredImg90);
title('Filtro de Prewitt (90 grados)');
subplot(3, 2, 5);
imshow(imagen_gris);
title('Imagen Original en Gris');
subplot(3, 2, 6);
imshow(finalImg);
title('Imagen Sumada');
