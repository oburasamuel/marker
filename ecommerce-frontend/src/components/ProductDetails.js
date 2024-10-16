import React from 'react';
import { useParams } from 'react-router-dom';
import { useQuery } from '@apollo/client';
import { GET_PRODUCT_DETAILS } from '../graphql/queries';

const ProductDetails = () => {
  const { id } = useParams();
  const { loading, error, data } = useQuery(GET_PRODUCT_DETAILS, {
    variables: { id }
  });

  if (loading) return <p>Loading product details...</p>;
  if (error) return <p>Error loading product details</p>;

  const { product } = data;

  return (
    <div className="product-details">
      <img src={product.imageUrl} alt={product.name} />
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p><strong>Price:</strong> ${product.price}</p>
      <p><strong>Stock:</strong> {product.stock}</p>
      <button className="add-to-cart-btn">Add to Cart</button>
    </div>
  );
};

export default ProductDetails;
