using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;



namespace test
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
     
        OpenFileDialog file = new OpenFileDialog();
      
        Bitmap image;
        string filename;

          string[] X = new string[] { "", "", "","" };



        private void button2_Click_1(object sender, System.EventArgs e)
        {
         

        }




       

      



        private void button3_Click(object sender, System.EventArgs e)
        {
            this.Close();
        }




        private void timer1_Tick(object sender, System.EventArgs e)
        {
           
        }

        private void button4_Click(object sender, System.EventArgs e)
        {
            
        }

        private void button4_Click_1(object sender, System.EventArgs e)
        {
           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click_2(object sender, EventArgs e)
        {
            if (X[0] == "")
            {
                MessageBox.Show("no data");


            }
            else
            {

                richTextBox1.Clear();
                string fn = "C:/Users/windows.10/Desktop/data - Copy.txt";
                int nx = 3;  // Number predictor variables
                int nc = 3;  // Number classes
                int N = 24;  // Number data items
                string[][] data = LoadData(fn, N, nx + 1, ',');



                int[][] jointCts = MatrixInt(nx, nc);
                int[] yCts = new int[nc];



                for (int i = 0; i < N; ++i)
                {
                    int y = int.Parse(data[i][nx]);
                    ++yCts[y];
                    for (int j = 0; j < nx; ++j)
                    {
                        if (data[i][j] == X[j])
                            ++jointCts[j][y];
                    }
                }
                // Laplacian smoothing
                for (int i = 0; i < nx; ++i)
                    for (int j = 0; j < nc; ++j)
                        ++jointCts[i][j];




                // Compute evidence terms
                double[] eTerms = new double[nc];
                for (int k = 0; k < nc; ++k)
                {
                    double v = 1.0;
                    for (int j = 0; j < nx; ++j)
                    {
                        v *= (double)(jointCts[j][k]) / (yCts[k] + nx);
                    }
                    v *= (double)(yCts[k]) / N;
                    eTerms[k] = v;
                }



                double evidence = 0.0;
                for (int k = 0; k < nc; ++k)
                    evidence += eTerms[k];
                double[] probs = new double[nc];
                for (int k = 0; k < nc; ++k)
                    probs[k] = eTerms[k] / evidence;

                // richTextBox1.AppendText("Probabilities: ");
                // for (int k = 0; k < nc; ++k)
                //   richTextBox1.AppendText( probs[k].ToString("F4") + "     ");
                //richTextBox1.AppendText("\n");
                richTextBox1.AppendText("Probabilities: % ");
                for (int k = 0; k < nc; ++k)
                    richTextBox1.AppendText(((probs[k] * 100)) + "     ");
                richTextBox1.AppendText("\n");


                int pc = ArgMax(probs);
                richTextBox1.AppendText("Predicted class: ");
                richTextBox1.AppendText(pc.ToString());
                if (pc == 0)
                {
                    richTextBox1.AppendText("\n");
                    richTextBox1.AppendText("eczema");
                    richTextBox2.AppendText("الاكزيما: 1- لا تحك المنطقة المصابة 2- قم بترطيب بشرتك بانتظام 3- تجنب الاستحمام بمياه ساخنة جدا 4- لا تقم بالاستحمام لمدة تزيد عن عشر دقائق 5- ارتد ملابس قطنية 6- تجنب استخدام منتجات التقشير");
                }

                if (pc == 1)
                {
                    richTextBox1.AppendText("\n");
                    richTextBox1.AppendText("cancer ");
                    richTextBox2.AppendText("سرطان الجلد بأنواعه: لا تعرض الممنطقة المصابة لأشعة الشمس ولا لأجهزة التسمير 2- قم بتطبيق واقي شمسي في حال ستتعرض المنطقة المصابة للشمس 3- راجع طبيب الجلدية بأسرع وقت لأخذ خزعة وفحصها مجهريا والتأكد من الحالة المرضية ");
                }
                if (pc == 2)
                {
                    richTextBox1.AppendText("\n");
                    richTextBox1.AppendText("psoriasis");
                    richTextBox2.AppendText("الصدفية: 1- لا تحق المنطقة المصابة 2- خذ حماما يوميا لمدة لا تزيد عن عشر دقائق 3- قم بتغطية المنطقة المصابة عند النوم 4- عرض المنطقة لكمية قليلة من أشعة الشمس بفترة بعد الضهيرة أو الصباح الباكر 5- تجنب تناول منتجات الألبان");

                }
                for (int t=0;t<3;t++)
                {
                    X[t] = "";


                }
            }
              
            } 
            static string[][] MatrixString(int rows, int cols)
            {
                string[][] result = new string[rows][];
                for (int i = 0; i < rows; ++i)
                    result[i] = new string[cols];
                return result;
            }
            static int[][] MatrixInt(int rows, int cols)
            {
                int[][] result = new int[rows][];
                for (int i = 0; i < rows; ++i)
                    result[i] = new int[cols];
                return result;
            }
            static string[][] LoadData(string fn, int rows,int cols, char delimit)
            {
                string[][] result = MatrixString(rows, cols);
                FileStream ifs = new FileStream(fn, FileMode.Open);
                StreamReader sr = new StreamReader(ifs);
                string[] tokens = null;
                string line = null;
                int i = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    tokens = line.Split(delimit);
                   
                    for (int j = 0; j < cols; ++j)
                        result[i][j] = tokens[j];
                    
                    ++i;
                }
                sr.Close(); ifs.Close();
                return result;
            }
            static int ArgMax(double[] vector)
            {
                int result = 0;
                double maxV = vector[0];
                for (int i = 0; i < vector.Length; ++i)
                {
                    if (vector[i] > maxV)
                    {
                        maxV = vector[i];
                        result = i;
                    }
                }
                return result;
            }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            X[0]="b";
        }

        private void checkBox8_CheckedChanged(object sender, EventArgs e)
        {
         X[0]="a";
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
             X[1]="B";
        }

        private void checkBox7_CheckedChanged(object sender, EventArgs e)
        {
             X[1]="A";
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
             X[2]="e";
        }

        private void checkBox6_CheckedChanged(object sender, EventArgs e)
        {
             X[2]="d";
        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
             X[2]="D";
        }

        private void checkBox5_CheckedChanged(object sender, EventArgs e)
        {
             X[2]="d";
        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void a3_CheckedChanged(object sender, EventArgs e)
        {
            X[0] = "c";
        }

        private void h3_CheckedChanged(object sender, EventArgs e)
        {
            X[0] = "C";
        }
    }






    }




        
    

