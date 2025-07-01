#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

void a(char *buffer, size_t buffer_size) {
    snprintf(buffer, buffer_size, "{\"temperature\": 25, \"humidity\": 60, \"condition\": \"Sunny\"}");
}

void b(const char *url, const char *data) {
    CURL *curl;
    CURLcode res;

    curl = curl_easy_init();
    if (curl) {
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");

        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }

        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Failed to initialize CURL\n");
    }
}

int main() {
    const char *api_url = "https://example.com/weather-api";
    char weather_data[256];

    a(weather_data, sizeof(weather_data));
    printf("Weather Data: %s\n", weather_data);

    b(api_url, weather_data);

    return 0;
}
