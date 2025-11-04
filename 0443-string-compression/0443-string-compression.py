class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        write = 0
        read = 0

        while read < n:
            ch = chars[read]
            start = read
            while read < n and chars[read] == ch:
                read += 1
            count = read - start

            chars[write] = ch
            write += 1

            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1

        return write
        