LANG = {
    "id": {
        "app_title": "Transformasi Matriks dalam Pengolahan Citra",

        "app_intro": """
Aplikasi multipage ini mendemonstrasikan **transformasi geometrik** menggunakan matriks homogen 3×3
(translasi, skala, rotasi, shear, refleksi) serta **filter berbasis konvolusi** (blur dan sharpen)
yang diimplementasikan secara manual menggunakan kernel.

**Cara menggunakan**
- Buka halaman **Image Processing** untuk mengunggah gambar dan mencoba transformasi/filter.
- Transformasi diterapkan menggunakan matriks dengan inverse mapping dan bilinear sampling.
- Blur dan sharpen menggunakan kernel konvolusi manual (tanpa fungsi bawaan).
        
**Tujuan pembelajaran**
- Memahami representasi transformasi afine 2D menggunakan matriks (koordinat homogen).
- Melatih penerapan kernel konvolusi pada citra digital.
""",

        "matrix_brief_title": "Transformasi Matriks (ringkas)",
        "matrix_brief_desc": """
- Matriks 3×3 digunakan pada koordinat homogen `[x, y, 1]`
  untuk menggabungkan translasi dengan transformasi linear.
""",

        "conv_brief_title": "Konvolusi (ringkas)",
        "conv_brief_desc": """
- Konvolusi dilakukan dengan menggeser kernel pada citra dan menjumlahkan hasil perkalian elemen.
- Contoh kernel:
    - Blur (rata-rata 3×3): `1/9 * ones((3,3))`
    - Sharpen: `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]`
""",

        "cta_image_page": "Silakan lanjut ke halaman **Image Processing** untuk mencoba transformasi dan filter."
    },

    "en": {
        "app_title": "Matrix Transformations in Image Processing",

        "app_intro": """
This multi-page application demonstrates **geometric transformations** using 3×3 homogeneous matrices
(translation, scaling, rotation, shearing, reflection) and **convolution-based filters** (blur and sharpen)
implemented manually using kernels.

**How to use**
- Go to the **Image Processing** page to upload an image and try transformations/filters.
- Transformations are applied using matrices with inverse mapping and bilinear sampling.
- Blur and sharpen use manual convolution kernels (no built-in functions).

**Learning objectives**
- Understand how 2D affine transformations are represented using matrices (homogeneous coordinates).
- Practice implementing convolution kernels for digital images.
""",

        "matrix_brief_title": "Matrix transformations (brief)",
        "matrix_brief_desc": """
- 3×3 matrices are applied to homogeneous coordinates `[x, y, 1]`
  to combine translation with linear transformations.
""",

        "conv_brief_title": "Convolution (brief)",
        "conv_brief_desc": """
- Convolution is implemented by sliding a kernel over the image and summing element-wise products.
- Example kernels:
    - Blur (3×3 average): `1/9 * ones((3,3))`
    - Sharpen: `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]`
""",

        "cta_image_page": "Now go to the **Image Processing** page to try transformations and filters."
    }
}
