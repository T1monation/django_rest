import React from 'react'
import { Link } from 'react-router-dom'


const AuthorItem = ({ author }) => {
    console.log(author, author.id)
    return (
        <tr>
            <td>
                <Link to={`author/${author.id}`} >{author.id}</Link>
            </td>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr >
    )
}

const AuthorList = ({ authors }) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                First Name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}
export default AuthorList
