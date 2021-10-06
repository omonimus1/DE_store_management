using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DE
{
    class Product
    {
        public int ProductId { get; set; }
        public string ProductName { get; set; }
        public int OrderId { get; set; }
        public int Quantity { get; set; }

        public static Product GetProduct()
        {
            Product product = new Product() { ProductId = 01, ProductName = "C# Book", OrderId = 02, Quantity = 2 };
            return product;
        }
    }
}
