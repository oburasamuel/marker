import { gql } from '@apollo/client';

// Query to fetch all products
export const GET_PRODUCTS = gql`
  query GetProducts {
    products {
      id
      name
      price
      description
      stock
      imageUrl
    }
  }
`;

// Query to fetch product details
export const GET_PRODUCT_DETAILS = gql`
  query GetProductDetails($id: ID!) {
    product(id: $id) {
      id
      name
      price
      description
      stock
      imageUrl
    }
  }
`;
