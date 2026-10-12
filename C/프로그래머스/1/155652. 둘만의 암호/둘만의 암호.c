#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* s, const char* skip, int index) {
    bool excluded[26] = {false};
    char alphabet[26];
    char converted[26] = {0};
    int count = 0;

    for (size_t i = 0; skip[i] != '\0'; i++) {
        excluded[skip[i] - 'a'] = true;
    }

    for (int i = 0; i < 26; i++) {
        if (!excluded[i]) {
            alphabet[count++] = (char)('a' + i);
        }
    }

    // 3. 알파벳별 변환 결과를 미리 계산
    int shift = index % count;

    for (int i = 0; i < count; i++) {
        converted[alphabet[i] - 'a'] =
            alphabet[(i + shift) % count];
    }

    size_t length = strlen(s);
    char* answer = malloc(length + 1);

    if (answer == NULL) {
        return NULL;
    }

    for (size_t i = 0; i < length; i++) {
        answer[i] = converted[s[i] - 'a'];
    }

    answer[length] = '\0';
    return answer;
}