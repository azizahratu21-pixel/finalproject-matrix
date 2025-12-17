# languages.py

LANG = {

    # ======================================================
    # INDONESIAN
    # ======================================================
    "id": {

        # ================= APP (HOME) =================
        "app_title": "Transformasi Matriks dalam Pengolahan Gambar",

        "app_intro": (
            "Aplikasi multi-halaman ini mendemonstrasikan **transformasi geometris** "
            "menggunakan matriks homogen 3×3 (translasi, skala, rotasi, geser, dan refleksi) "
            "serta **filter berbasis konvolusi** seperti blur dan sharpen. "
            "Seluruh proses diimplementasikan secara manual untuk memperkuat pemahaman "
            "konsep **Aljabar Linear dalam Pengolahan Gambar**."
        ),

        "matrix_brief_title": "Transformasi Matriks (Ringkas)",
        "matrix_brief_desc": (
            "Transformasi geometris dua dimensi direpresentasikan menggunakan "
            "matriks 3×3 pada koordinat homogen [x, y, 1]. "
            "Pendekatan ini memungkinkan translasi dikombinasikan dengan "
            "transformasi linier lainnya dalam satu matriks."
        ),

        "conv_brief_title": "Konvolusi (Ringkas)",
        "conv_brief_desc": (
            "Konvolusi adalah operasi dasar dalam pengolahan gambar yang dilakukan "
            "dengan menggeser kernel di atas gambar dan menjumlahkan hasil "
            "perkalian elemen-elemen yang bersesuaian."
        ),

        "cta_image_page": (
            "Silakan buka halaman **Image Processing** untuk mencoba langsung "
            "transformasi matriks dan filter konvolusi pada gambar."
        ),

        # ================= IMAGE PROCESSING PAGE =================
        "ip_title": "Pengolahan Gambar Berbasis Transformasi Matriks",

        "upload_image": "Unggah gambar",
        "upload_hint": "Silakan unggah gambar terlebih dahulu.",

        "transform_order": "**Urutan transformasi matriks**",
        "order_mode": "Mode urutan",
        "preset_order": "Urutan default",
        "custom_order": "Urutan kustom",
        "select_order": "Pilih urutan transformasi",

        "translation": "Translasi",
        "enable_translation": "Aktifkan translasi",

        "scaling": "Skala",
        "enable_scaling": "Aktifkan skala",
        "scale_center": "Skala terhadap pusat gambar",

        "rotation": "Rotasi",
        "enable_rotation": "Aktifkan rotasi",
        "angle": "Sudut rotasi (derajat)",

        "shearing": "Geser (Shearing)",
        "enable_shearing": "Aktifkan shearing",

        "reflection": "Refleksi",
        "enable_reflection": "Aktifkan refleksi",
        "axis": "Sumbu refleksi",

        "filters": "Filter Konvolusi",
        "blur": "Blur",
        "sharpen": "Sharpen",

        "apply": "Terapkan",
        "preview": "Pratinjau",

        "original": "Gambar Asli",
        "result": "Hasil Transformasi",

        "matrix_used": "**Matriks transformasi total yang digunakan:**",
    },

    # ======================================================
    # ENGLISH
    # ======================================================
    "en": {

        # ================= APP (HOME) =================
        "app_title": "Matrix Transformations in Image Processing",

        "app_intro": (
            "This multi-page application demonstrates **geometric transformations** "
            "using 3×3 homogeneous matrices (translation, scaling, rotation, shearing, and reflection) "
            "as well as **convolution-based filters** such as blur and sharpen. "
            "All processes are implemented manually to strengthen understanding of "
            "**Linear Algebra concepts in Image Processing**."
        ),

        "matrix_brief_title": "Matrix Transformations (Brief)",
        "matrix_brief_desc": (
            "Two-dimensional geometric transformations are represented using "
            "3×3 matrices on homogeneous coordinates [x, y, 1]. "
            "This allows translation to be combined with other linear "
            "transformations within a single matrix."
        ),

        "conv_brief_title": "Convolution (Brief)",
        "conv_brief_desc": (
            "Convolution is a fundamental operation in image processing, "
            "performed by sliding a kernel over an image and summing the "
            "element-wise products."
        ),

        "cta_image_page": (
            "Go to the **Image Processing** page to directly experiment with "
            "matrix transformations and convolution filters on images."
        ),

        # ================= IMAGE PROCESSING PAGE =================
        "ip_title": "Image Processing Using Matrix Transformations",

        "upload_image": "Upload image",
        "upload_hint": "Please upload an image first.",

        "transform_order": "**Transformation order**",
        "order_mode": "Order mode",
        "preset_order": "Preset order",
        "custom_order": "Custom order",
        "select_order": "Select transformation order",

        "translation": "Translation",
        "enable_translation": "Enable translation",

        "scaling": "Scaling",
        "enable_scaling": "Enable scaling",
        "scale_center": "Scale about image center",

        "rotation": "Rotation",
        "enable_rotation": "Enable rotation",
        "angle": "Rotation angle (degrees)",

        "shearing": "Shearing",
        "enable_shearing": "Enable shearing",

        "reflection": "Reflection",
        "enable_reflection": "Enable reflection",
        "axis": "Reflection axis",

        "filters": "Convolution Filters",
        "blur": "Blur",
        "sharpen": "Sharpen",

        "apply": "Apply",
        "preview": "Preview",

        "original": "Original Image",
        "result": "Transformed Image",

        "matrix_used": "**Total transformation matrix used:**",
    }
}

