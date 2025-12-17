# languages.py

LANG = {

    # ======================================================
    # INDONESIAN
    # ======================================================
    "id": {

        # ----------------------
        # APP (HOME)
        # ----------------------
        "app_title": "Transformasi Matriks dalam Pengolahan Gambar",
        "app_desc": (
            "Aplikasi multi-halaman ini mendemonstrasikan **transformasi geometris** "
            "menggunakan matriks homogen 3×3 (translasi, skala, rotasi, geser, refleksi) "
            "serta **filter berbasis konvolusi** (blur dan sharpen) yang diimplementasikan "
            "secara manual tanpa menggunakan fungsi bawaan pengolahan gambar."
        ),

        "how_to_use": "Cara penggunaan",
        "how_to_use_desc": (
            "- Buka halaman **Image Processing** untuk mengunggah gambar.\n"
            "- Pilih transformasi dan filter yang diinginkan.\n"
            "- Transformasi diterapkan menggunakan matriks dan inverse mapping.\n"
            "- Filter blur dan sharpen diimplementasikan menggunakan kernel konvolusi."
        ),

        "learning_goals": "Tujuan pembelajaran",
        "learning_goals_desc": (
            "- Memahami representasi transformasi afin 2D menggunakan matriks homogen.\n"
            "- Memahami hubungan antara aljabar linear dan pengolahan gambar.\n"
            "- Mengimplementasikan operasi konvolusi secara manual."
        ),

        "matrix_brief": "Transformasi matriks (ringkas)",
        "matrix_brief_desc": (
            "Transformasi geometris direpresentasikan menggunakan matriks 3×3 "
            "pada koordinat homogen [x, y, 1]."
        ),

        "conv_brief": "Konvolusi (ringkas)",
        "conv_brief_desc": (
            "Konvolusi dilakukan dengan menggeser kernel di atas gambar dan "
            "menghitung jumlah hasil perkalian elemen."
        ),

        "go_to_ip": "Silakan buka halaman **Image Processing** untuk mencoba transformasi dan filter.",

        # ----------------------
        # IMAGE PROCESSING PAGE
        # ----------------------
        "ip_title": "Alat Pengolahan Gambar",

        "upload_image": "Unggah gambar (PNG/JPG)",
        "upload_hint": "Unggah gambar untuk memulai. Disarankan ukuran kecil (mis. 400×400) agar proses lebih cepat.",

        "preview": "Pratinjau",

        "transform_order": "**Urutan transformasi**: pilih urutan penerapan transformasi.",
        "order_mode": "Mode urutan:",
        "preset_order": "Preset: Translasi → Skala → Rotasi → Geser → Refleksi",
        "custom_order": "Urutan kustom",
        "select_order": "Pilih urutan transformasi",

        "translation": "Translasi",
        "enable_translation": "Aktifkan translasi",

        "scaling": "Skala",
        "enable_scaling": "Aktifkan skala",
        "scale_center": "Skala terhadap pusat gambar",

        "rotation": "Rotasi",
        "enable_rotation": "Aktifkan rotasi",
        "angle": "Sudut (derajat)",

        "shearing": "Geser (Shearing)",
        "enable_shearing": "Aktifkan geser",

        "reflection": "Refleksi",
        "enable_reflection": "Aktifkan refleksi",
        "axis": "Sumbu / garis refleksi",

        "filters": "Filter (Konvolusi)",
        "blur": "Blur (rata-rata 3×3)",
        "sharpen": "Sharpen",

        "apply": "Terapkan operasi",

        "original": "Gambar asli (RGBA)",
        "result": "Gambar hasil transformasi / filter",

        "matrix_used": "**Matriks transformasi (3×3) yang diterapkan:**"
    },

    # ======================================================
    # ENGLISH
    # ======================================================
    "en": {

        # ----------------------
        # APP (HOME)
        # ----------------------
        "app_title": "Matrix Transformations in Image Processing",
        "app_desc": (
            "This multi-page application demonstrates **geometric transformations** "
            "using 3×3 homogeneous matrices (translation, scaling, rotation, shearing, reflection) "
            "and **convolution-based filters** (blur and sharpen) implemented manually "
            "without relying on built-in image processing functions."
        ),

        "how_to_use": "How to use",
        "how_to_use_desc": (
            "- Go to the **Image Processing** page to upload an image.\n"
            "- Select the desired transformations and filters.\n"
            "- Transformations are applied using matrices and inverse mapping.\n"
            "- Blur and sharpen are implemented using convolution kernels."
        ),

        "learning_goals": "Learning objectives",
        "learning_goals_desc": (
            "- Understand 2D affine transformations using homogeneous matrices.\n"
            "- Understand the relationship between linear algebra and image processing.\n"
            "- Implement convolution operations manually."
        ),

        "matrix_brief": "Matrix transformations (brief)",
        "matrix_brief_desc": (
            "Geometric transformations are represented using 3×3 matrices "
            "on homogeneous coordinates [x, y, 1]."
        ),

        "conv_brief": "Convolution (brief)",
        "conv_brief_desc": (
            "Convolution is performed by sliding a kernel over the image "
            "and summing element-wise products."
        ),

        "go_to_ip": "Go to the **Image Processing** page to try transformations and filters.",

        # ----------------------
        # IMAGE PROCESSING PAGE
        # ----------------------
        "ip_title": "Image Processing Tools",

        "upload_image": "Upload image (PNG/JPG)",
        "upload_hint": "Upload an image to start. Small images (e.g. 400×400) are recommended for faster processing.",

        "preview": "Preview",

        "transform_order": "**Transformation order**: choose the order in which transformations are applied.",
        "order_mode": "Order mode:",
        "preset_order": "Preset: Translation → Scaling → Rotation → Shearing → Reflection",
        "custom_order": "Custom order",
        "select_order": "Select transformation order",

        "translation": "Translation",
        "enable_translation": "Enable translation",

        "scaling": "Scaling",
        "enable_scaling": "Enable scaling",
        "scale_center": "Scale about image center",

        "rotation": "Rotation",
        "enable_rotation": "Enable rotation",
        "angle": "Angle (degrees)",

        "shearing": "Shearing",
        "enable_shearing": "Enable shearing",

        "reflection": "Reflection",
        "enable_reflection": "Enable reflection",
        "axis": "Axis / reflection line",

        "filters": "Filters (Convolution)",
        "blur": "Blur (3×3 average)",
        "sharpen": "Sharpen",

        "apply": "Apply operations",

        "original": "Original image (RGBA)",
        "result": "Transformed / filtered image",

        "matrix_used": "**Applied transformation matrix (3×3):**"
    }
}
