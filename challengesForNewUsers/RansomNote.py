

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNoteList = list(ransomNote)
        ransomNoteList.sort()

        magazineList = list(magazine)
        magazineList.sort()
        print(ransomNoteList)
        print(magazineList)

        i = 0
        for rs in ransomNoteList:

            while i < len(magazineList):
                if rs == magazineList[i]:
                    i += 1
                    break

                elif rs > magazineList[i]:
                    i += 1

                else:
                    return False
            else:
                return False

        return True


if __name__ == "__main__":
    ransomNote = "az"
    magazine = "ab"

    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))