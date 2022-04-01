import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(1000) * 100
y = np.random.normal(50, 10, 1000)

print("%3.2f %3.2f" % (x.mean(), y.mean()))

fig, (hist, text) = plt.subplots(1, 2)
hist.hist(x, bins=20, alpha=0.5)
hist.hist(y, bins=20, alpha=0.5)
hist.legend(("Uniform Distribution", "Normal Distribution"))
hist.set_ylabel("Samples per bin")
hist.set_xlabel("Bins")
hist.set_title("Uniform vs. Normal Distributions")

text.text(0, -.1, "Question 1:\n\n"
                  "\"X = np.random.rand(1000) * 100\"\n\n"
                  "generates 1000 values between 0 and 1\n"
                  "with uniform distribution. Then multiplies\n"
                  "each value by 100, creating an array of\n"
                  "1000 random variables between 0 and 100\n\n"
                  "\"Y = np.random.normal(50, 10, 1000)\"\n\n"
                  "generates 1000 values between\n"
                  "0 and 1 with normal distribution\n"
                  " and then multiplies each value\n"
                  "value by 100, creating an array\n"
                  "of 1000 random variables between \n"
                  "0 and 100"
                  "\n\nQuestion 2:\n\n"
                  "X mean = %3.2f X std %3.2f\n"
                  "Y mean = %3.2f, Y std = %3.2f\n\n"
                "Question 4:\n\n"
                "X is rectangular and Y is gaussian"
          % (x.mean(), x.std(), y.mean(), y.std()))
text.set_clip_on(False)
text.axis('off')
text.set_title("Answers:")

plt.show()
