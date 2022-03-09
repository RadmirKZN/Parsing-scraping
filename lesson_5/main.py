import requests
import img2pdf


def get_data():
    headers = {
        "Accept": "image / avif, image / webp, * / *",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
    }

    img_list = []
    for i in range(1, 51):
        url = f"https://kabinet-faberlic.com/flipbook/catalog-faberlic-4-2022-belarus/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Downloaded {i} of 48")
    print("#" * 20)
    print(img_list)

#create PDF file

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))
    print("PDF file created successfully!")


# def write_to_pdf():
#     print(os.listdir(media))
#     img_list = [f"media/{i}.jpg" for i in range(1, 49)]
#     print(img_list)
#
#     with open("result.pdf", "wb") as f:
#         f.write(img2pdf.convert(img_list))
#     print("PDF file created successfully!")


def main():
    get_data()


if __name__ == '__main__':
    main()