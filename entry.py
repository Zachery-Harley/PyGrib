from streams.grib2_file_input_stream import Grib2FileInputStream
from streams.grib2_input_stream import Grib2InputStream

if __name__ == "__main__":
    print("Running")

    inputStream: Grib2InputStream = Grib2FileInputStream("./resources/ground-temperature.grib2")
    print(inputStream.end_of_file())
