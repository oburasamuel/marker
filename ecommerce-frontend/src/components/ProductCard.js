import React from 'react';
import { Link } from 'react-router-dom';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <img src={product.imageUrl} alt={product.name} />
      <h3>{product.name}</h3>
      <p>${product.price}</p>
      <Link to={`/products/${product.id}`}>
        <button className="details-btn">View Details</button>
      </Link>
    </div>
    
  );
};

export default ProductCard;
